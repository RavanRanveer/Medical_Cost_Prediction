import streamlit as st
import pickle
import numpy as np
from xgboost import XGBRegressor

# Load the trained model and preprocessor
model_path = "/Users/ravanranveer/Downloads/Model/xgboost_model.json"
preprocessor_path = "/Users/ravanranveer/Downloads/Model/preprocessor.pkl"

model = XGBRegressor()
model.load_model(model_path)



# Streamlit app
st.title("Out-of-Pocket Expenditure Predictor")

# Demographics Section
st.header("Demographics")

age = st.number_input("Age", min_value=0, max_value=120, value=25)
bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=25.0)
region = st.selectbox("Region", ["Northeast", "Midwest", "South", "West"])
race = st.selectbox("Race", ["White", "Black", "Asian", "Other"])
gender = st.selectbox("Gender", ["Male", "Female"])
marital_status = st.selectbox("Marital Status", ["Married", "Divorced", "Single", "Widowed"])
born_in_usa = st.selectbox("Born in USA", ["Yes", "No"])

# Health Conditions Section
st.header("Health Conditions")

hypertension = st.selectbox("High Blood Pressure Diagnosis", ["Yes", "No"])
coronary_heart_disease = st.selectbox("Coronary Heart Disease Diagnosis", ["Yes", "No"])
angina = st.selectbox("Angina Diagnosis", ["Yes", "No"])
heart_attack = st.selectbox("Heart Attack Diagnosis", ["Yes", "No"])
other_heart_disease = st.selectbox("Other Heart Disease Diagnosis", ["Yes", "No"])
stroke = st.selectbox("Stroke Diagnosis", ["Yes", "No"])
emphysema = st.selectbox("Emphysema Diagnosis", ["Yes", "No"])
chronic_bronchitis = st.selectbox("Chronic Bronchitis Diagnosis", ["Yes", "No"])
high_cholesterol = st.selectbox("High Cholesterol Diagnosis", ["Yes", "No"])
any_cancer = st.selectbox("Any Cancer Diagnosis", ["Yes", "No"])
diabetes = st.selectbox("Diabetes Diagnosis", ["Yes", "No"])
arthritis = st.selectbox("Arthritis Diagnosis", ["Yes", "No"])
asthma = st.selectbox("Asthma Diagnosis", ["Yes", "No"])
walking_limitation = st.selectbox("Walking Limitation", ["Yes", "No"])

# General Health Questions
st.header("General Health Questions")

smoking_status = st.selectbox(
    "How Often Do You Smoke Cigarettes?",
    ["Every Day", "Some Days", "Not At All"]
)
covid_vaccine = st.selectbox("Have You Received a COVID-19 Vaccine?", ["Yes", "No"])
alcohol_consumption = st.selectbox(
    "Alcohol Consumption",
    ["Never", "Less Than Monthly", "Monthly", "Weekly", "Daily"]
)

# Health Care and Insurance
st.header("Health Care and Insurance")

healthcare_provider = st.selectbox("Do You Have a Healthcare Provider?", ["Yes", "No"])
primary_care_provider = st.selectbox("Primary Care Provider Type", ["Person", "Facility", "None"])
insurance_coverage_status = st.selectbox("Insurance Coverage Status", ["Yes", "No"])
insurance_type = st.selectbox("Insurance Type", ["Private", "Public", "Uninsured"])

# Prediction button
if st.button("Predict"):
    # Prepare input for prediction
    input_data = np.array([[
        age, bmi, region, race, gender, marital_status, born_in_usa,
        hypertension, coronary_heart_disease, angina, heart_attack, other_heart_disease,
        stroke, emphysema, chronic_bronchitis, high_cholesterol, any_cancer,
        diabetes, arthritis, asthma, walking_limitation, smoking_status, covid_vaccine,
        alcohol_consumption, healthcare_provider, primary_care_provider,
        insurance_coverage_status, insurance_type
    ]])

    # Apply preprocessing
    
    # Predict
    prediction = model.predict(input_data)
    
    # Display the result
    st.subheader(f"Predicted Out-of-Pocket Expenditure: ${prediction[0]:.2f}")