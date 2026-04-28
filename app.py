import streamlit as st
import joblib
import numpy as np

model = joblib.load("linearmodel.pkl")

st.title("Salary Prediction App")

st.divider()

st.write("With this app, you can get estimations for the salaries of the company employees")

years = st.number_input("Enter the no of years at the company",min_value = 0, step = 1, value = 1)
jobrate = st.number_input("Enter the Job rate", min_value = 0.0, step = 0.5, value = 3.5)

st.divider()

predict = st.button("Press the button for salary prediction")

st.divider()

if predict:
    X = [years,jobrate]
    X1 = np.array([X])
    prediction = model.predict(X1)[0]
    st.write(f"Salary prediciton is {prediction:,.2f}")
    st.balloons()
else:
    st.write("Please enter the values and use predict button")
