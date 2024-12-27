import matplotlib.pyplot as plt
import seaborn as sns
from main import merged_data

# Public Health Expenditure vs Life Expectancy
def PHEvsLE():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_data, x='Health Expenditure (% GDP)', y='Life Expectancy', 
                    hue='Country Name', style='Country Name', s=100, alpha=0.6)

    # adding leniear regretion line
    sns.regplot(data=merged_data, x='Health Expenditure (% GDP)', y='Life Expectancy',
                scatter=False, color='red', line_kws={'linestyle': '--', 'label': 'Trend Line'}, ci=95)

    # correlation coefficient
    correlation = merged_data['Health Expenditure (% GDP)'].corr(merged_data['Life Expectancy'])
    stats_text = f'Correlation: {correlation:.2f}'
    plt.text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8), verticalalignment='top')

    plt.title('Public Health Expenditure vs Life Expectancy')
    plt.xlabel('Public Health Expenditure (% GDP)')
    plt.ylabel('Life Expectancy')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

# Public Health Expenditure vs Happiness
def PHEvsH():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_data, x='Health Expenditure (% GDP)', y='Life Ladder', 
                    hue='Country Name', style='Country Name', s=100, alpha=0.6)

    # adding leniear regretion line
    sns.regplot(data=merged_data, x='Health Expenditure (% GDP)', y='Life Ladder',
                scatter=False, color='red', line_kws={'linestyle': '--', 'label': 'Trend Line'}, ci=95)

    # correlation coefficient
    correlation = merged_data['Health Expenditure (% GDP)'].corr(merged_data['Life Ladder'])
    stats_text = f'Correlation: {correlation:.2f}'
    plt.text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8), verticalalignment='top')

    plt.title('Public Health Expenditure vs Happiness')
    plt.xlabel('Public Health Expenditure (% GDP)')
    plt.ylabel('Happiness')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

# Happiness vs Life Expectancy
def HvsLE():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_data, x='Life Expectancy', y='Life Ladder', 
                    hue='Country Name', style='Country Name', s=100, alpha=0.6)

    # adding leniear regretion line
    sns.regplot(data=merged_data, x='Life Expectancy', y='Life Ladder',
                scatter=False, color='red', line_kws={'linestyle': '--', 'label': 'Trend Line'}, ci=95)

    # correlation coefficient
    correlation = merged_data['Life Expectancy'].corr(merged_data['Life Ladder'])
    stats_text = f'Correlation: {correlation:.2f}'
    plt.text(0.05, 0.95, stats_text, transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8), verticalalignment='top')

    plt.title('Life Expectancy vs Happiness')
    plt.xlabel('Life Expectancy')
    plt.ylabel('Life Ladder')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

# OOP Expenditure vs Current Health Expenditure size is Health Expenditure (% GDP)
def OOPEvsCHE():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged_data, x='OOP Expenditure', y='Current Health Expenditure', 
                    size='Health Expenditure (% GDP)', sizes=(50, 500),
                    hue='Country Name', style='Country Name', s=100, alpha=0.6)
    
    plt.title('OOP Expenditure vs Current Health Expenditure ($ PPP adjusted), size represents Health Expenditure (% GDP)')
    plt.xlabel('OOP Expenditure')
    plt.ylabel('Current Health Expenditure')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

# bouble size is happiness, Life Expectancy vs Health Expenditure (% GDP)
def HvsLEvsHE():
    plt.figure(figsize=(12, 8))
    bubble_chart = sns.scatterplot(data=merged_data, x='Health Expenditure (% GDP)', 
                                    y='Life Expectancy', size='Life Ladder', 
                                    hue='Country Name', alpha=0.7, sizes=(50, 500))
    plt.title('Public Health Expenditure vs Life Expectancy, bouble size represents Happiness')
    plt.xlabel('Public Health Expenditure (% GDP)')
    plt.ylabel('Life Expectancy')
    plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

OOPEvsCHE()
HvsLEvsHE()
PHEvsLE()
PHEvsH()
HvsLE()


