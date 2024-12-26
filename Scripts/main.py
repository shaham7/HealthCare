import pandas as pd

world_happiness_report_by_countries = pd.read_csv('Data/World_happiness_report_2024.csv')
Life_Expectancy_by_countries = pd.read_csv('Data/LE.csv')
public_health_expenditure_share_of_total_gdp = pd.read_csv('Data/public-health-expenditure-share-gdp.csv')
Out_of_pocket_expenditure_per_capita_PPP_adjusted = pd.read_csv('Data/Out-of-pocket expenditure per capita, PPP (current international $).csv')
Current_health_expenditure_per_capita_PPP = pd.read_csv('Data/Current_health_expenditure_per_capita_PPP.csv')

# Countries and years I am going to work with 
countries = ['United States', 'United Kingdom', 'Japan', 'Netherlands', 
             'Finland', 'Australia', 'Singapore', 'India', 'South Korea']
years = list(range(2015, 2022))