import pandas as pd
import re

world_happiness_report_by_countries = pd.read_csv('Data/World_happiness_report_2024.csv')
Life_Expectancy_by_countries = pd.read_csv('Data/LE.csv')
public_health_expenditure_share_of_total_gdp = pd.read_csv('Data/public-health-expenditure-share-gdp.csv')
Out_of_pocket_expenditure_per_capita_PPP_adjusted = pd.read_csv('Data/Out-of-pocket expenditure per capita, PPP (current international $).csv')
Current_health_expenditure_per_capita_PPP = pd.read_csv('Data/Current_health_expenditure_per_capita_PPP.csv')

# print(public_health_expenditure_share_of_total_gdp['Entity'].unique().tolist())

# Countries and years i am going to work with 
countries = ['United Kingdom', 'Japan', 'Denmark',
             'Finland', 'Australia', 'India', 'Canada', 'Germany', 'China', 
             'Brazil','Italy', 'Spain', 'Argentina', 'Belgium', 'France']

# countries = public_health_expenditure_share_of_total_gdp['Entity'].unique()

years = list(range(2015, 2022))

# filtering by countires 
happiness = world_happiness_report_by_countries[world_happiness_report_by_countries['Country name'].isin(countries)]
life_expectancy = Life_Expectancy_by_countries[Life_Expectancy_by_countries['Country Name'].isin(countries)]
health_expenditure = public_health_expenditure_share_of_total_gdp[public_health_expenditure_share_of_total_gdp['Entity'].isin(countries)]
oop_expenditure = Out_of_pocket_expenditure_per_capita_PPP_adjusted[Out_of_pocket_expenditure_per_capita_PPP_adjusted['Country Name'].isin(countries)]
current_health_expenditure = Current_health_expenditure_per_capita_PPP[Current_health_expenditure_per_capita_PPP['Country Name'].isin(countries)]

# filtering the filtered dataset by years
happiness = happiness[happiness['year'].isin(years)]
life_expectancy = life_expectancy[['Country Name', 'Country Code'] + [str(year) for year in years]]
health_expenditure = health_expenditure[health_expenditure['Year'].isin(years)]
oop_expenditure = oop_expenditure[['Country Name', 'Country Code'] + [f'{year} [YR{year}]' for year in years]]
current_health_expenditure = current_health_expenditure[['Country Name', 'Country Code'] + [f'{year} [YR{year}]' for year in years]]

# renaming columns for consistency in data
happiness.rename(columns={'Country name': 'Country Name', 'year': 'Year'}, inplace=True)
health_expenditure.rename(columns={'Entity': 'Country Name', 'public_health_expenditure_pc_gdp': 'Health Expenditure (% GDP)'}, inplace=True)
oop_expenditure.columns = oop_expenditure.columns.str.replace(r" \[YR(\d+)\]", "", regex=True)
current_health_expenditure.columns = current_health_expenditure.columns.str.replace(r" \[YR(\d+)\]", "", regex=True)

# melting datasets for consistancy
life_expectancy = life_expectancy.melt(id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='Life Expectancy')
oop_expenditure = oop_expenditure.melt(id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='OOP Expenditure')
current_health_expenditure = current_health_expenditure.melt(id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='Current Health Expenditure')

life_expectancy['Year'] = life_expectancy['Year'].astype(int)
oop_expenditure['Year'] = life_expectancy['Year'].astype(int)
current_health_expenditure['Year'] = life_expectancy['Year'].astype(int)
current_health_expenditure['Current Health Expenditure'] = pd.to_numeric(current_health_expenditure['Current Health Expenditure'], errors='coerce')
oop_expenditure['OOP Expenditure'] = pd.to_numeric(oop_expenditure['OOP Expenditure'], errors='coerce')

# merging all datasets into one 
merged_data = happiness.merge(life_expectancy, on=['Country Name', 'Year'], how='inner')
merged_data = merged_data.merge(health_expenditure, on=['Country Name', 'Year'], how='inner')
merged_data = merged_data.merge(oop_expenditure, on=['Country Name', 'Year'], how='inner')
merged_data = merged_data.merge(current_health_expenditure, on=['Country Name', 'Year'], how='inner')

# Save the cleaned and merged dataset
# merged_data.to_csv('cleaned_merged_data.csv', index=False)

# print(merged_data.dtypes)