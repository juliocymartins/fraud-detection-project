# App Folder – Fraud Detection App

This folder contains all the necessary files to run the Fraud Detection web application built with **Streamlit**. The app loads a pre-trained machine learning model and provides a user-friendly interface for users to input transaction data or test entire files.

## Contents

- `fraud_app.py`: Main Streamlit application script that loads the saved model and handles user input.
- `fraud_rf_model.pkl`: Serialized pipeline and trained model using Random Forest.
- `background_fraud.jpg`: Background image used to visually enhance the Streamlit interface.
- `test_fraud_yes.xlsx`: Example dataset with **fraudulent** transactions to test the app.
- `test_fraud_no.xlsx`: Example dataset with **non-fraudulent** transactions to test the app.

## How to Run Locally

From the root of the project:

```bash
streamlit run app/fraud_app.py