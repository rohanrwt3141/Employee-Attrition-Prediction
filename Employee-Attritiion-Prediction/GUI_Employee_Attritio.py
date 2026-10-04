import streamlit as st
import joblib as jl
import pandas as pd
from plotly.graph_objs.indicator.gauge import threshold

st.set_page_config(page_title="Employee Attrition Prediction", layout="wide")
st.title("Employee Atrrition Prediction", text_alignment = "center")

model = jl.load("/home/rohan/PyCharmMiscProject/.venv/AIML/Employees_Attrition_Prediction.pkl")

st.divider()
st.subheader("🤠 PERSONAL INFORMATION")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Enter Your Age:", value = 18, min_value = 18)

    travel = st.selectbox("Enter The Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])

    drate = st.number_input("Enter Your Daily Rate:", value = 100, min_value = 0)

    dept = st.selectbox("Enter your Department", ['Sales', 'Research & Development', 'Human Resources'])

    distance = st.number_input("Enter Your Distance from Home:", value = 1, min_value = 0)

    edu = st.selectbox("Enter your Education", [1, 2, 3, 4, 5])

    edufield = st.selectbox("Enter your Education Field", ['Life Sciences', 'Other', 'Medical', 'Marketing',
       'Technical Degree', 'Human Resources'])


with col2:

    envsat = st.selectbox("Enter your Environment Satisfaction", [1, 2, 3, 4, 5])

    gender = st.selectbox("Enter your Gender", ['Male', 'Female'])

    hrate = st.number_input("Enter your House Rate:", value = 1, min_value = 0)

    jobi = st.selectbox("Enter your Job Involvement", [1, 2, 3, 4, 5])

    jobl = st.selectbox("Enter your Job Level", [1, 2, 3, 4, 5])

    jobRole = st.selectbox("Enter your Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
       'Manufacturing Director', 'Healthcare Representative', 'Manager',
       'Sales Representative', 'Research Director', 'Human Resources'])

    jobsa = st.selectbox("Enter your Job Satisfaction", [1, 2, 3, 4, 5])

with col3:

    marital = st.selectbox("Enter your Marital", ["Single", "Married", "Divorced"])

    monIncome = st.number_input("Enter your Income", value = 100, min_value = 0)

    MonthRate = st.number_input("Enter your Monthly Rate", value = 1, min_value = 0)

    numcomp = st.number_input("Enter your Number of Companies", value = 1, min_value = 0)

    over = st.selectbox("Enter your Overtime", ["Yes", "No"])

    hike = st.number_input("Enter your Salary Hike Percentage", value = 0, min_value = 0)

    performance = st.selectbox("Enter your Performance Rate", [1, 2, 3, 4, 5])

st.divider()
st.subheader("🏤 WORK INFORMATION")

col4, col5, col6 = st.columns(3)

with col4:

    relation = st.selectbox("Enter your Relationship Satisfaction", [1, 2, 3, 4, 5])

    stock = st.selectbox("Enter your Stock Level", [0, 1, 2, 3])

    yearincurr = st.number_input("Enter your Year in Current Role", value = 0, min_value = 0)

with col5:

    workingyear = st.number_input("Enter your Working Year", value = 0, min_value = 0)

    training = st.number_input("Enter your Training Year", value = 0, min_value = 0)

    yearpromotion = st.number_input("Enter your Year Since Last Promotion", value = 0, min_value = 0)

with col6:

    worklife = st.selectbox("Enter your Work Life Balance", [1, 2, 3, 4])

    yearatcompany = st.number_input("Enter your Year of Companies", value = 0, min_value = 0)

    yearMana = st.number_input("Enter your Year with Current Manager", value = 0, min_value = 0)

if st.button("🪄 Predict", use_container_width = True):
    input = {"Age": [age], "BusinessTravel": [travel], "DailyRate": [drate], "Department": [dept],
             "DistanceFromHome": [distance], "Education": [edu], "EducationField": [edufield], "EnvironmentSatisfaction": [envsat],
             "Gender": [gender], "HourlyRate": [hrate], "JobInvolvement": [jobi], "JobLevel": [jobl], "JobRole": [jobRole],
             "JobSatisfaction": [jobsa], "MaritalStatus": [marital], "MonthlyIncome": [monIncome], "MonthlyRate": [MonthRate], "NumCompaniesWorked": [numcomp],
             "OverTime": [over], "PercentSalaryHike": [hike], "PerformanceRating": [performance], "RelationshipSatisfaction": [relation],
              "StockOptionLevel": [stock], "TotalWorkingYears": [workingyear], "TrainingTimesLastYear": [training], "WorkLifeBalance": [worklife], "YearsAtCompany": [yearatcompany], "YearsInCurrentRole": [yearincurr]
             , "YearsSinceLastPromotion": [yearpromotion], "YearsWithCurrManager": [yearMana]}

    df_input = pd.DataFrame(input)
    probability = model.predict_proba(df_input)[0, 1]

    threshold = 0.1

    prediction = int(probability >= threshold)

    st.divider()

    c1, c2 = st.columns(2)
    with c1:
        if prediction == 1:
            st.error("High Risk To Leave")
        else:
            st.success("Low Risk To Leave")

    with c2:
        st.metric("Probability", probability * 100)
        st.progress(float(probability))