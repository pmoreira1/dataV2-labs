import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Define some file locations so all the downloaded and untreated data stays in the same place
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads\\')
DATA_FOLDER = os.path.join(os.getcwd(), 'data\\')

# Step 1. Covid Data
# Grab data from Kaggle platform using API
# This will grab and unzip the files we need. We will only use covid_19_data.csv

api = KaggleApi()
api.authenticate()
api.dataset_download_files('sudalairajkumar/novel-corona-virus-2019-dataset',
                           path=DOWNLOAD_FOLDER,
                           quiet=True,
                           unzip=True)

# Check if the file we want for covid exists
covid_tempfile = os.path.join(DOWNLOAD_FOLDER, 'covid_19_data.csv')
covid_file = os.path.join(DATA_FOLDER, 'covid.csv')

if os.path.exists(covid_tempfile):
    covid_data = pd.read_csv(covid_tempfile)
    # Province/State has a lot of NaN values. Makes sense to drop it because we will do Country Level analysis
    covid_data.drop('Province/State', axis=1, inplace=True)
    # We need some country cleanup so let's create a dictionary to allow a better rename
    country_dict = {"('St. Martin',)": 'St. Martin', "Mainland China": 'China', " Azerbaijan": 'Azerbaijan',
                    'occupied Palestinian territory': 'Palestine'}
    # Replace the relavant names
    covid_data['Country/Region'] = covid_data['Country/Region'].replace(country_dict)
    # Convert ObservationDate to datetime object
    covid_data['ObservationDate'] = pd.to_datetime(covid_data['ObservationDate'], format='%m/%d/%Y')
    # Drop Last Update because we are going to group it so we wont be needing it
    covid_data.drop('Last Update', axis=1, inplace=True)
    # Let's rename a few columns
    covid_data.rename(columns={
        'Country/Region': 'Country',
        'ObservationDate': 'RegisteredDate'
    }, inplace=True)
    # Group by date and country so we have a nice time series
    covid_data = covid_data.groupby(['Country', 'RegisteredDate'])[['Confirmed', 'Deaths', 'Recovered']].agg('sum').reset_index()
    # Create a new field with the amount of active cases on each day
    covid_data['Active'] = covid_data['Confirmed'] - (covid_data['Deaths'] + covid_data['Recovered'])
    # Save it to csv in the data folder
    covid_data.to_csv(covid_file)
else:
    print("Missing new data for Covid 19")

# Step 2 -  Grab world population data
# Read from file  API_SP.POP.TOTL_DS2_en_csv_v2_887275.csv and save a much compact version
# world_population_url = 'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'

population_tempfile = os.path.join(DOWNLOAD_FOLDER,  'API_SP.POP.TOTL_DS2_en_csv_v2_887275.csv')
population_file = os.path.join(DATA_FOLDER, 'population.csv')
eu_countries = ['Austria', 'Italy', 'Belgium', 'Latvia', 'Bulgaria', 'Lithuania', 'Croatia', 'Luxembourg', 'Cyprus', 'Malta', 'Czech Republic', 'Netherlands', 'Denmark', 'Poland', 'Estonia', 'Portugal', 'Finland', 'Romania', 'France', 'Slovakia', 'Germany', 'Slovenia', 'Greece', 'Spain', 'Hungary', 'Sweden', 'Ireland']
if os.path.exists(population_tempfile):
    population_data = pd.read_csv(population_tempfile)
    # Grab only data for 2018
    population_data = population_data[['Country Name', '2018']]
    # Drop Na values since we will not be able to use them anyway
    population_data.dropna(inplace=True)
    # Rename a few columns
    population_data.rename(columns={
        'Country Name': 'Country',
        '2018': 'Population'
    }, inplace=True)
    # Convert data to int
    population_data['EU'] = population_data.apply(lambda x: '1' if x['Country'] in eu_countries else '0', axis=1)
    population_data.to_csv(population_file)
else:
    print("Missing Population data file")