import pandas as pd
import numpy as np
import os


confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

confirmed = pd.melt(confirmed, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Confimred')
deaths = pd.melt(deaths, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Deaths')

combined = confirmed.merge(deaths, on=['Province/State', 'Country/Region', 'Lat', 'Long', 'Date'], how='outer')
combined = combined[['Country/Region', 'Date', 'Confimred', 'Deaths']]

os.system('git pull')
combined.to_csv('data.csv', index=False)
os.system('git add .')
os.system('git commit -m "Auto update"')
os.system('git push')
