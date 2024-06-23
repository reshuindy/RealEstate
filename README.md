# RealEstate
Real Estate Price Prediction Model
Overview
This repository contains the code and resources for a machine learning model that predicts real estate sale prices based on town and residential type. The primary objective of this project is to provide accurate sale price estimates for stakeholders, such as homebuyers, real estate agents, and property investors, by leveraging historical sales data.

**MVP Description**
The Minimum Viable Product (MVP) of this project includes:

A trained Linear regression model that predicts sale prices based on input features: town and residential type.
A user-friendly interface where users can input the town and residential type to get an estimated sale price.
Comprehensive data preprocessing, including handling missing values and encoding categorical features.
Model evaluation metrics to assess performance and ensure reliability.

**How It Was Built**
Data Collection and Preprocessing
Data Sources: Historical real estate sales data containing fields such as town, residential type, and sale amount.
Preprocessing Steps:
Handling missing values.
Encoding categorical variables (town, residential type) using techniques like one-hot encoding.
Normalizing numerical features to ensure consistent scaling.
Model Training
Algorithm: Random Forest Regression
Libraries Used: scikit-learn, pandas, numpy
Steps:
Split the data into training and testing sets.
Train the Random Forest model on the training set.
Evaluate the model using the testing set to ensure accuracy and reliability.
Model Evaluation
Metrics:
Feature Matrix
Coefficient Matrix 

Validation: Cross-validation to assess model performance and ensure it generalizes well to unseen data.
User Interface
Interface: Simple command-line interface for MVP; plans to develop a web-based UI.
Functionality: Users input the town and residential type to receive the estimated sale price.
**Future Work**
Develop a web-based interface for user interaction.
Expand feature set for better prediction accuracy.
Implement regular data updates and model retraining pipelines.
Explore and potentially integrate more advanced machine learning models for enhanced performance.

**How will you set up this project in your system?**
**System Requirement : **WINDOW,MAC or Linux system with minimum 8 GB RAM 256 Secondory Memory.
**Installation : **
  1. Python 3.9.13 or greater (https://www.python.org/downloads/)
     ----------------------
     % python --version
      Python 3.9.13
    ---------------------- 

  3. Streamlit, version 1.35.0 (https://docs.streamlit.io/get-started/installation)
     --------------------------
     % streamlit --version
      Streamlit, version 1.35.0
     ----------------------------
  4. Install the RealEstate code in your system (https://github.com/reshuindy/RealEstate.git)
     project name - RealEstate
    (Git help :https://docs.github.com/en/repositories)
    Note :
     >Update data_path vaiable of each source file  of project - main.py,1_dashboard.py,Price_estimator.py and new_predict.py for data file path of local system.
     >data_path is defined in starting of each source file. like
     data_path = '/Users/XXXXXX/XXXXXX/Real_Estate_Sales_2001-2021_GL.csv' 

**  Run/deploy code : **
   Run the following commnad to start the application: streamlit run main.py
   -----------------------------------------------
    You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.240:8501

/Users/XXXXXXXX/Desktop/workspacePython/realstate/main.py:6: DtypeWarning: Columns (8,9,10,11,12) have mixed types. Specify dtype option on import or set low_memory=False.
  data = pd.read_csv(data_path)
  -----------------------------------------------------
Browse the link http://localhost:8501 to see the application
