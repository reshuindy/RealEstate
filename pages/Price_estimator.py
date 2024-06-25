import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Path to the data
#data_path = '/Users/utkarsh/Desktop/Real_Estate_Sales_2001-2021_GL.csv'
data_path = './data/rs_data.csv'

# Title of the page
st.title("Welcome to the Real Estate Sales Price Estimator")

# Load the data
data = pd.read_csv(data_path)

# Drop unnecessary columns
columns_to_drop = ['NoUseCode', 'AssessorRemarks', 'OPMremarks', 'Location']
data = data.drop(columns=columns_to_drop)

# Remove rows with null values in specified columns
data = data.dropna(subset=['Town', 'ResidentialType', 'SaleAmount', 'ListYear'])

# Encode categorical data
label_encoder_town = LabelEncoder()
label_encoder_residential_type = LabelEncoder()

data['Town'] = label_encoder_town.fit_transform(data['Town'])
data['ResidentialType'] = label_encoder_residential_type.fit_transform(data['ResidentialType'])

# Split the data into features and target
X = data[['Town', 'ResidentialType', 'ListYear']]
y = data['SaleAmount']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Sidebar for input
st.sidebar.header('Estimate Property Sales Price')

# Dropdowns for town and residential type
selected_town = st.sidebar.selectbox("Select Town", label_encoder_town.classes_)
selected_residential_type = st.sidebar.selectbox("Select Residential Type", label_encoder_residential_type.classes_)
selected_list_year = st.sidebar.number_input("Select List Year", min_value=int(data['ListYear'].min()), max_value=int(data['ListYear'].max()), step=1)

# Transform input data
input_data = pd.DataFrame({
    'Town': [selected_town],
    'ResidentialType': [selected_residential_type],
    'ListYear': [selected_list_year]
})
input_data['Town'] = label_encoder_town.transform(input_data['Town'])
input_data['ResidentialType'] = label_encoder_residential_type.transform(input_data['ResidentialType'])

# Predict the sale amount
predicted_sale_amount = model.predict(input_data)[0]

# Display the prediction
st.write("## Estimated Sales Price")
st.write(f"The estimated sales price for a {selected_residential_type} in {selected_town} listed in {selected_list_year} is ${predicted_sale_amount:.2f}")
