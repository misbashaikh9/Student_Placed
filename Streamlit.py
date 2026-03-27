import streamlit as st
import requests

st.title("🎓 Placement Predictor")

# Inputs
cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
aptitude = st.slider("Aptitude Score", 0, 100, 70)
communication = st.slider("Communication", 1, 10, 5)
projects = st.slider("Projects", 0, 5, 2)

# Predict button
if st.button("Predict"):
    url = "https://student-placed-1-043h.onrender.com/predict"

    data = {
        "cgpa": cgpa,
        "aptitude": aptitude,
        "communication": communication,
        "projects": projects
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()

        if result['placement_prediction'] == 1:
            st.success("Student is likely to be Placed")
        else:
            st.error(" Student is NOT likely to be Placed")
    else:
        st.error("API Error")
