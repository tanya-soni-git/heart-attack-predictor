# 💓 Heart Attack Risk Predictor

This project is a Machine Learning–based web application that predicts the risk of a heart attack based on patient health parameters. Built using **Streamlit**, it allows users to input data through an interactive interface and get real-time risk predictions.

## 🚀 Live Demo

👉 [Launch the App](https://heart-attack-predictor-2nxkdzvgkct9xr4j2gthcg.streamlit.app/)  


---

## 📊 Features

- Predicts the **likelihood of a heart attack** based on medical attributes.
- User-friendly **Streamlit web interface**.
- Real-time prediction and probability output.
- Fully interactive sliders and dropdowns.
- **Trained model** included (`model.pkl`) for deployment.

---

## 📥 Input Parameters

| Feature        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Age            | Age of the patient                                                         |
| Sex            | Male / Female                                                              |
| Chest Pain     | Typical Angina, Atypical Angina, Non-Anginal Pain, Asymptomatic             |
| Resting BP     | Resting blood pressure (in mm Hg)                                          |
| Cholesterol    | Serum cholesterol in mg/dl                                                 |
| Fasting Sugar  | Whether fasting blood sugar > 120 mg/dl (True/False)                       |
| Resting ECG    | Normal, ST-T abnormality, or LV hypertrophy                                |
| Max HR         | Maximum heart rate achieved                                                |
| Exercise Angina| Yes / No                                                                   |
| Old Peak       | ST depression induced by exercise relative to rest                         |
| Slope          | Slope of the peak exercise ST segment                                      |
| Major Vessels  | Number of major vessels colored by fluoroscopy (0–4)                       |
| Thalassemia    | Normal, Fixed defect, or Reversible defect                                 |

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn** (for model training)
- **Streamlit** (for UI)
- **Matplotlib/Seaborn** (for EDA)
- **Git & GitHub** (for version control and collaboration)

---

## 📁 Project Structure

heart-attack-predictor/
│
├── heart_attack_app.py # Streamlit web app
├── model.pkl # Trained Random Forest model
├── model_columns.pkl # Column names used for prediction
├── requirements.txt # Required Python packages
└── README.md # Project documentation


---

## ⚙️ Installation & Running Locally

1. **Clone the repository**

```bash 
git clone https://github.com/your-username/heart-attack-predictor.git
cd heart-attack-predictor

2. **Install dependencies**

```pip install -r requirements.txt

3. **Run the app**
```streamlit run heart_attack_app.py


📌 Notes
Make sure model.pkl and model_columns.pkl are present in the root directory.

The model was trained using a processed heart disease dataset (based on UCI repository).

## 📓 Notebook

The full Jupyter notebook with data cleaning, visualization, model training, and evaluation is available here:

[📘 heart_attack_analysis.ipynb](./heart_attack_analysis.ipynb)


🧑‍💻 Author
Tanya Soni
Pursuing MCA | Passionate about AI, ML, and Web Technologies
https://www.linkedin.com/in/tanya-soni-link/

📜 License
This project is open-source and available under the MIT License.
