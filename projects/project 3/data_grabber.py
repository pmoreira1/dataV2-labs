import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Define some file locations so all the downloaded and untreated data stays in the same place
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads\\')
DATA_FOLDER = os.path.join(os.getcwd(), 'data\\')

# Define some functions to allow cleaner calculation of daily increase of cases


def do_variance_calc(old, new):
    if new > 0:
        return round(float(((new - old) / ((new + old) / 2)) * 100), 2), new-old
    else:
        return 0, 0


def calculate_day_variance(row):
    fields = ['Confirmed', 'Recovered', 'Active', 'Deaths']
    prev_date = row['RegisteredDate'] - pd.DateOffset(1)
    cur_country = row['Country']
    percentage_result = {}
    count_result = {}
    # Check if previous record exists
    if ((covid_data['RegisteredDate'] == prev_date) & (covid_data['Country'] == cur_country)).any():
        prev_record = covid_data[(covid_data['RegisteredDate'] == prev_date) & (covid_data['Country'] == cur_country)]
        for i, f in enumerate(fields):
            percentage_result[i], count_result[i] = do_variance_calc(prev_record[f].item(), row[f])
        return percentage_result[0], count_result[0], percentage_result[1], count_result[1], percentage_result[2], count_result[2],  percentage_result[3], count_result[3]
    else:
        return 0, 0, 0, 0, 0, 0, 0, 0


def calculate_days(row):
    country = row['Country']
    date = row['RegisteredDate']
    # Get min date which will be the first record for that country
    first_case_date = pd.to_datetime(covid_data[covid_data['Country'] == country]['RegisteredDate'].min(), format='%Y-%m-%d')
    days_since = date - first_case_date
    return days_since.days


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
                    'occupied Palestinian territory': 'Palestine', 'US': 'United States', 'UK': 'United Kingdom'}
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
    # Calculate variance for desired fields
    covid_data[['ConfirmedIncrease%', 'ConfirmedIncrease', 'RecoveredIncrease%', 'RecoveredIncrease',
                'ActiveIncrease%', 'ActiveIncrease', 'DeathsIncrease%', 'DeathsIncrease']] = covid_data.apply(
        lambda x: calculate_day_variance(x), axis=1, result_type='expand')

    # Create Days since first case column
    covid_data['DaysSinceFirst'] = covid_data.apply(lambda x: calculate_days(x), axis=1, result_type='expand')
    # Save it to csv in the data folder
    covid_data.to_csv(covid_file)
else:
    print("Missing new data for Covid 19")

# Step 2 -  Grab world population data
# Read from file  API_SP.POP.TOTL_DS2_en_csv_v2_887275.csv and save a much compact version
# world_population_url = 'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'

population_tempfile = os.path.join(DOWNLOAD_FOLDER,  'API_SP.POP.TOTL_DS2_en_csv_v2_887275.csv')
population_file = os.path.join(DATA_FOLDER, 'population.csv')
eu_countries = ['Austria', 'Italy', 'Belgium', 'Latvia', 'Bulgaria', 'Lithuania', 'Croatia', 'Luxembourg', 'Cyprus',
                'Malta', 'Czech Republic', 'Netherlands', 'Denmark', 'Poland', 'Estonia', 'Portugal', 'Finland',
                'Romania', 'France', 'Slovakia', 'Germany', 'Slovenia', 'Greece', 'Spain', 'Hungary',
                'Sweden', 'Ireland']

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


# Step 3 - Grab Government measures
# Load excel file from https://www.bsg.ox.ac.uk/sites/default/files/OxCGRT_Download_latest_data.xlsx
# Clean data and store it as local csv
# Load Excel directly in pandas
measures_tempfile = 'https://www.bsg.ox.ac.uk/sites/default/files/OxCGRT_Download_latest_data.xlsx'
# measures_tempfile = os.path.join(DOWNLOAD_FOLDER, 'OxCGRT_Download_latest_data.xlsx')
measures_file = os.path.join(DATA_FOLDER, 'measures.csv')

measure_data = pd.read_excel(measures_tempfile)
# Drop Columns we don't need
measure_data.drop(['CountryCode', 'ConfirmedCases', 'ConfirmedDeaths', 'Unnamed: 34', 'S8_Fiscal measures', 'S8_Notes',
                    'S9_Monetary measures', 'S9_Notes', 'S10_Emergency investment in health care', 'S10_Notes',
                    'S11_Investment in Vaccines', 'S11_Notes', 'S1_Notes', 'S2_Notes', 'S3_Notes', 'S4_Notes',
                    'S5_Notes', 'S6_Notes', 'S7_Notes', 'S1_IsGeneral', 'S2_IsGeneral', 'S3_IsGeneral', 'S4_IsGeneral',
                    'S5_IsGeneral', 'S6_IsGeneral'], axis=1, inplace=True)

# Find columns that start with S
scols = [col for col in measure_data.columns if 'S' in col]
# Drop rows with only NaN
measure_data = measure_data.drop(measure_data[measure_data.filter(like='S').isna().all(1)].index)
# Fill NaN with 0
measure_data.fillna(0, inplace=True)
# Convert cols to int
measure_data[scols] = measure_data[scols].astype(int)
# Drop StringencyIndex from this list since we don't need to change anything else on that column values
scols.remove('StringencyIndex')
# Change int to short description for tableau tooltip
measure_data[scols] = measure_data[scols].replace({0: 'No', 1: 'Yes', 2: 'Yes', 3: 'Yes', 4: 'Yes'})
# Change Date to datetime object
measure_data['Date'] = pd.to_datetime(measure_data['Date'], format='%Y%m%d')
# Rename columns
measure_data.rename(columns={
    'CountryName': 'Country',
    'Date': 'MeasureDate',
    'S1_School closing': 'Schools Closed',
    'S2_Workplace closing': 'Workplace Closed',
    'S3_Cancel public events': 'Public Events Cancelled',
    'S4_Close public transport': 'Public Transportation Stopped',
    'S5_Public information campaigns': 'Public Information Campaigns',
    'S6_Restrictions on internal movement': 'Internal Travel Restriction',
    'S7_International travel controls': 'International Travel Control',
    'StringencyIndex': 'StrictnessLevel'
}, inplace=True)
# Reset index and drop old index
measure_data.reset_index(inplace=True)
measure_data.drop('index', axis=1, inplace=True)
# Save to csv
measure_data.to_csv(measures_file)
