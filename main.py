import streamlit as st
import pandas as pd

# Load data
data_path = '/Users/utkarsh/Desktop/Real_Estate_Sales_2001-2021_GL.csv'
data = pd.read_csv(data_path)

# Drop unnecessary columns
columns_to_drop = ['Non Use Code', 'Assessor Remarks', 'OPM remarks', 'Location']
data = data.drop(columns=columns_to_drop)

# Remove rows with null values in specified columns
data = data.dropna(subset=['Address', 'Property Type', 'Residential Type'])

st.title("Real Estate Sales Data (2001-2021)")

st.image('/Users/utkarsh/Desktop/header_image_3.jpeg', caption='Real Estate', use_column_width=True)


# Show the dataset
st.header("Dataset")
st.write(data.head())