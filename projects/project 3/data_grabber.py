import os

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Define some file locations so all the downloaded and untreated data stays in the same place
download_folder = os.path.join(os.getcwd(), 'downloads\\')
covid_filename = 'covid_19_data.csv'
covid_file = os.path.join(download_folder, covid_filename)

world_population_url = 'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv'


# Step 1. Covid Data
# api = KaggleApi()
# api.authenticate()
# api.dataset_download_files('sudalairajkumar/novel-corona-virus-2019-dataset',
#                            path=download_folder,
#                            quiet=True,
#                            unzip=True)

# Check if the file we want exists

if os.path.exists(covid_file):
    covid_data = pd.read_csv(covid_file)
    print(covid_data.head())

