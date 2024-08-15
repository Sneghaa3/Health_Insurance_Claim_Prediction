# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:21:48 2024

@author: ATCHAYAA THINGAL
"""

import numpy as np
import pickle
import streamlit as st

# Load the trained model from disk
loaded_model = pickle.load(open(r"trained_model.sav", 'rb'))

# Function for prediction
def insurance_cost_prediction(input_data):
    # Prepare the input data as a nested list
    input_data = np.array(input_data).reshape(1, -1)

    # Make the prediction
    prediction = loaded_model.predict(input_data)

    return float(prediction[0])

def main():
    # Title of the web app
    st.title("Insurance Cost Prediction Web App")

    # Input widgets for each feature
    age = st.number_input("Enter Age", min_value=0)
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    bmi = st.number_input("Enter BMI", min_value=0.0)
    children = st.number_input("Enter Number of Children", min_value=0)
    smoker = st.selectbox("Are you a smoker?", ["Yes", "No"])
    region = st.selectbox("Select Region", ["Southeast", "Southwest", "Northeast", "Northwest"])

    # Mapping user-friendly labels to model's expected numerical values
    gender_map = {"Male": 0, "Female": 1}
    smoker_map = {"Yes": 0, "No": 1}
    region_map = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}

    # Convert user input to numerical values for the model
    Gender = gender_map[gender]
    Smoker = smoker_map[smoker]
    Region = region_map[region]

    # Prepare the input data
    input_data = [age, Gender, bmi, children, Smoker, Region]

    # Code for prediction
    result = None

   # Creating a button for prediction
    if st.button("Get Prediction"):
        result = insurance_cost_prediction(input_data)
        if isinstance(result, (int, float)):  # Check if result is numeric
            st.success(f'The predicted insurance cost is: ${result:.2f}')
        else:
            st.error("Prediction result is not a valid number.")


if __name__ == '__main__':
    main()
