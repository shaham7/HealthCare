import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from scipy.stats import linregress

merged_data = pd.read_csv('cleaned_merged_data.csv')


def regression_line(fig, x, y, df):
    slope, intercept, r_value, _, _ = linregress(df[x], df[y])
    line_x = [df[x].min(), df[x].max()]
    line_y = [slope * xi + intercept for xi in line_x]
    fig.add_trace(
        go.Scatter(x=line_x, y=line_y,
            mode="lines",
            name=f"Trend Line (r={r_value:.2f})",
            line=dict(color="red", dash="dash"),
        )
    )

def PHEvsLE_plotly(data=merged_data):
    fig = px.scatter(
        data,
        x='Health Expenditure (% GDP)', y='Life Expectancy',
        color='Country Name', symbol='Country Name',
        title='Public Health Expenditure vs Life Expectancy',
        labels={'Health Expenditure (% GDP)': 'Public Health Expenditure (% GDP)', 'Life Expectancy': 'Life Expectancy'},
        template='plotly_white',
    )
    regression_line(fig, 'Health Expenditure (% GDP)', 'Life Expectancy', data)
    fig.update_layout(height=600,width=900)
    return fig

def PHEvsH_plotly(data=merged_data):
    fig = px.scatter(
        data,
        x='Health Expenditure (% GDP)',
        y='Life Ladder',
        color='Country Name',
        symbol='Country Name',
        title='Public Health Expenditure vs Happiness',
        labels={'Health Expenditure (% GDP)': 'Public Health Expenditure (% GDP)', 'Life Ladder': 'Happiness'},
        template='plotly_white',
    )
    regression_line(fig, 'Health Expenditure (% GDP)', 'Life Ladder', data)
    
    fig.update_layout(height=600,width=900)
    return fig

def HvsLE_plotly(data=merged_data):
    fig = px.scatter(
        data,
        x='Life Expectancy',
        y='Life Ladder',
        color='Country Name',
        symbol='Country Name',
        title='Happiness vs Life Expectancy',
        labels={'Life Expectancy': 'Life Expectancy', 'Life Ladder': 'Happiness'},
        template='plotly_white',
    )
    regression_line(fig, 'Life Expectancy', 'Life Ladder', data)
    fig.update_layout(height=600,width=900)
    return fig

def OOPEvsCHE_plotly(data=merged_data):
    fig = px.scatter(
        data,
        x='OOP Expenditure',
        y='Current Health Expenditure',
        size='Health Expenditure (% GDP)',
        color='Country Name',
        title='OOP Expenditure vs Current Health Expenditure',
        labels={'OOP Expenditure': 'OOP Expenditure ($ PPP adjusted)', 'Current Health Expenditure': 'Current Health Expenditure'},
        template='plotly_white',
    )
    fig.update_layout(height=600,width=900)
    return fig  # not adding regression line since it won't make sense for this plot.

def HvsLEvsHE_plotly(data=merged_data):
    fig = px.scatter(
        data,
        x='Health Expenditure (% GDP)',
        y='Life Expectancy',
        size='Life Ladder',
        color='Country Name',
        title='Life Expectancy vs Health Expenditure (% GDP) and Happiness',
        labels={'Health Expenditure (% GDP)': 'Public Health Expenditure (% GDP)', 'Life Expectancy': 'Life Expectancy'},
        template='plotly_white',
    )
    regression_line(fig, 'Health Expenditure (% GDP)', 'Life Expectancy', data)
    fig.update_layout(height=600,width=900)
    return fig

# Streamlit App Layout
st.title("Public Health and Happiness Dashboard")


# Sidebar for country selection
st.sidebar.title("Dashboard Filters")
available_countries = merged_data['Country Name'].unique()
selected_countries = st.sidebar.multiselect(
    "Select Countries to Display",
    options=available_countries,
    default=available_countries,
)

if len(selected_countries) < 1:
    st.warning(f"Please select at least 1 option. (Displaying all data by defalt)")
elif selected_countries: #check if list is not empty
    selected_countries_string = ", ".join(selected_countries)
    st.write(f"\n\n\n\n Showing results for : {selected_countries_string}")
else:
    st.write("Please select options.")

if len(selected_countries) >= 1:
    filtered_data = merged_data[merged_data['Country Name'].isin(selected_countries)]
else: 
    filtered_data = merged_data
st.sidebar.title("Dashboard Navigation")
options = st.sidebar.radio(
    "Select a Visualization:",
    [
        "Public Health Expenditure vs Life Expectancy",
        "Public Health Expenditure vs Happiness",
        "Happiness vs Life Expectancy",
        "Life Expectancy vs Health Expenditure and Happiness",
        "OOP Expenditure vs Current Health Expenditure",
    ]
)

if options == "Public Health Expenditure vs Life Expectancy":
    st.plotly_chart(PHEvsLE_plotly(filtered_data), use_container_width=True)

elif options == "Public Health Expenditure vs Happiness":
    st.plotly_chart(PHEvsH_plotly(filtered_data), use_container_width=True)

elif options == "Happiness vs Life Expectancy":
    st.plotly_chart(HvsLE_plotly(filtered_data), use_container_width=True)

elif options == "OOP Expenditure vs Current Health Expenditure":
    st.plotly_chart(OOPEvsCHE_plotly(filtered_data), use_container_width=True)

elif options == "Life Expectancy vs Health Expenditure and Happiness":
    st.plotly_chart(HvsLEvsHE_plotly(filtered_data), use_container_width=True)

st.sidebar.info(
    """
    This dashboard explores relationships between public health expenditure, 
    life expectancy, and happiness metrics across selected countries.
    """
)