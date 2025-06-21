import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load column names used during training
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)

st.set_page_config(page_title="Heart Attack Prediction", layout="centered")
st.title("💓 Heart Attack Risk Predictor")

st.write("This app predicts the risk of heart attack based on medical attributes.")

# Collect user input
age = st.slider("Age", 20, 100, 50)
sex = st.radio("Sex", ["Female", "Male"])

cp_map = {
    "Typical Angina": 1,
    "Atypical Angina": 2,
    "Non-Anginal Pain": 3,
    "Asymptomatic": 4
}
cp = st.selectbox("Chest Pain Type (cp)", list(cp_map.keys()))

trtbps = st.slider("Resting Blood Pressure (trtbps)", 80, 200, 120)
chol = st.slider("Cholesterol (chol)", 100, 600, 200)

fbs_map = {"True (> 120 mg/dl)": 1, "False (≤ 120 mg/dl)": 0}
fbs = st.radio("Fasting Blood Sugar (fbs)", list(fbs_map.keys()))

restecg_map = {
    "Normal": 0,
    "ST-T wave abnormality": 1,
    "Left ventricular hypertrophy": 2
}
restecg = st.selectbox("Resting ECG (restecg)", list(restecg_map.keys()))

thalachh = st.slider("Maximum Heart Rate Achieved (thalachh)", 70, 210, 150)

exang_map = {"Yes": 1, "No": 0}
exng = st.radio("Exercise Induced Angina (exang)", list(exang_map.keys()))

oldpeak = st.slider("Old Peak (ST depression)", 0.0, 6.0, 1.0, step=0.1)

slp = st.selectbox("Slope of the ST Segment (slp)", [0, 1, 2])

caa = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (ca)", [0, 1, 2, 3, 4])

thal_map = {
    "Normal (3)": 3,
    "Fixed Defect (6)": 6,
    "Reversible Defect (7)": 7
}
thal = st.selectbox("Thalassemia (thal)", list(thal_map.keys()))

# Convert sex to numeric
sex_val = 1 if sex == "Male" else 0

# Prepare input dictionary using mapped values
input_dict = {
    "age": age,
    "sex": sex_val,
    "cp": cp_map[cp],
    "trtbps": trtbps,
    "chol": chol,
    "fbs": fbs_map[fbs],
    "restecg": restecg_map[restecg],
    "thalachh": thalachh,
    "exng": exang_map[exng],
    "oldpeak": oldpeak,
    "slp": slp,
    "caa": caa,
    "thal": thal_map[thal]
}

# Convert to DataFrame and apply the same preprocessing as during training
input_df = pd.DataFrame([input_dict])
input_df_encoded = pd.get_dummies(input_df)

# Ensure input features match the training features
input_df_encoded = input_df_encoded.reindex(columns=model_columns, fill_value=0)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df_encoded)[0]
    probability = model.predict_proba(input_df_encoded)[0][1]

    result = "🚨 At Risk of Heart Attack" if prediction == 1 else "✅ Not at Risk"
    st.subheader(f"Prediction: {result}")
    st.write(f"Probability: **{probability:.2%}**")
