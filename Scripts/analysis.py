import matplotlib.pyplot as plt
import seaborn as sns
from main import merged_data

# Public Health Expenditure vs Life Expectancy
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_data, x='Health Expenditure (% GDP)', y='Life Expectancy', 
                hue='Country Name', style='Country Name', s=100)
plt.title('Public Health Expenditure vs Life Expectancy')
plt.xlabel('Public Health Expenditure (% GDP)')
plt.ylabel('Life Expectancy')
plt.legend(title='Country')
plt.grid(True)
# plt.show()

# Line chart over time Public Health Expenditure Trends
plt.figure(figsize=(12, 8))
sns.lineplot(data=merged_data, x='Year', y='Health Expenditure (% GDP)', hue='Country Name', marker='o')
plt.title('Public Health Expenditure Trends (2015–2021)')
plt.xlabel('Year')
plt.ylabel('Public Health Expenditure (% GDP)')
plt.grid(True)
plt.legend(title='Country')
# plt.show()

# Line chart over time Life Expectancy
plt.figure(figsize=(12, 8))
sns.lineplot(data=merged_data, x='Year', y='Life Expectancy', hue='Country Name', marker='o')
plt.title('Life Expectancy Trends (2015–2021)')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.grid(True)
plt.legend(title='Country')
# plt.show()

# bouble 
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(data=merged_data, x='Health Expenditure (% GDP)', 
                                y='Life Expectancy', size='Life Ladder', 
                                hue='Country Name', alpha=0.7, sizes=(50, 500))
plt.title('Public Health Expenditure vs Life Expectancy and Happiness')
plt.xlabel('Public Health Expenditure (% GDP)')
plt.ylabel('Life Expectancy')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Country')
# plt.show()


# happiness project is done 

# Correlation Heatmap
correlation_data = merged_data[['Life Ladder', 'Log GDP per capita',
                                'Healthy life expectancy at birth','Current Health Expenditure',
                                'OOP Expenditure',
                                'Health Expenditure (% GDP)', 'Life Expectancy']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', fmt=".2f", cbar_kws={'label': 'Correlation'})
plt.title('Correlation Heatmap of all Variables')
# plt.show()

