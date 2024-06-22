import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Path to the data
data_path = '/Users/utkarsh/Desktop/readEstdata.csv'

# Title of the page
st.title("Real Estate Sales Price Estimator")

# Load the data
data = pd.read_csv(data_path)

# Drop unnecessary columns
columns_to_drop = ['Non Use Code', 'Assessor Remarks', 'OPM remarks', 'Location', 'Date Recorded', 'Address']
data = data.drop(columns=columns_to_drop, errors='ignore')

# Remove rows with null values in specified columns
data = data.dropna(subset=['Town', 'Residential Type', 'Sale Amount', 'List Year'])

# Convert 'List Year' to integer if it's not already
data['List Year'] = data['List Year'].astype(int)

# Ensure 'Sale Amount' is a float
data['Sale Amount'] = data['Sale Amount'].astype(float)

# Check for any non-numeric columns and print them
non_numeric_columns = data.select_dtypes(include=['object']).columns
st.write("Non-numeric columns: ", non_numeric_columns)

# One-hot encode categorical features
data = pd.get_dummies(data, columns=['Town', 'Residential Type'], drop_first=True)

# Split the data into features and target
X = data.drop(columns=['Sale Amount'])
y = data['Sale Amount']

# Verify the features and target
st.write("## Features (X) and Target (y)")
st.write("X columns: ", X.columns)
st.write("y head: ", y.head())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Sidebar for input
st.sidebar.header('Estimate Property Sales Price')

# Get list of towns and residential types from the columns after get_dummies
town_columns = [col for col in X.columns if 'Town_' in col]
residential_columns = [col for col in X.columns if 'Residential Type_' in col]

# Extract unique towns and residential types from column names
towns = [col.split('_')[1] for col in town_columns]
residential_types = [col.split('_')[1] for col in residential_columns]

# Dropdowns for town and residential type
selected_town = st.sidebar.selectbox("Select Town", towns)
selected_residential_type = st.sidebar.selectbox("Select Residential Type", residential_types)
selected_list_year = st.sidebar.number_input("Select List Year", min_value=int(data['List Year'].min()), max_value=int(data['List Year'].max()), step=1)

# Create input data frame for prediction
input_data = pd.DataFrame(index=[0], columns=X.columns)
input_data = input_data.fillna(0)  # Fill all with 0 initially
input_data[f'Town_{selected_town}'] = 1
input_data[f'Residential Type_{selected_residential_type}'] = 1
input_data['List Year'] = selected_list_year

# Predict the sale amount
predicted_sale_amount = model.predict(input_data)[0]

# Display the prediction
st.write("## Estimated Sales Price")
st.write(f"The estimated sales price for a {selected_residential_type} in {selected_town} listed in {selected_list_year} is ${predicted_sale_amount:.2f}")
