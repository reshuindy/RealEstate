import streamlit as st
import pandas as pd



# Load data
#data_path = '/Users/utkarsh/Desktop/Real_Estate_Sales_2001-2021_GL.csv'
data_path = './data/rs_data.csv'
data = pd.read_csv(data_path)

# Drop unnecessary columns
columns_to_drop = ['NoUseCode', 'AssessorRemarks', 'OPMremarks', 'Location']
data = data.drop(columns=columns_to_drop)

# Remove rows with null values in specified columns
data = data.dropna(subset=['Address', 'PropertyType', 'ResidentialType'])



# Streamlit app
st.title("Real Estate Sales Data (2001-2021)")

# Show the dataset
st.header("Dataset")
st.write(data.head())

# Filter data by year
st.header("Filter by Year")
years = data['ListYear'].unique()
selected_year = st.selectbox("Select Year", years)
filtered_data = data[data['ListYear'] == selected_year]
st.write(filtered_data)

# Filter data by town
st.header("Filter by Town")
towns = data['Town'].unique()
selected_town = st.selectbox("Select Town", towns)
filtered_data_town = data[data['Town'] == selected_town]
st.write(filtered_data_town)

# Display specific columns
st.header("View Specific Columns")
columns = data.columns.tolist()
selected_columns = st.multiselect("Select Columns", columns, default=columns )
st.write(data[selected_columns])



# Plot data
st.header("Sales Amount Over Time")
st.line_chart(data.groupby('ListYear')['SaleAmount'].sum())
