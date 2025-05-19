import streamlit as st
import joblib
import pandas as pd
import base64

# ======== INSERT BACKGROUND IMAGE WITH TRANSPARENCY ========

def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        position: relative;
    }}

    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 0;
    }}

    .stApp > * {{
        position: relative;
        z-index: 1;
    }}

    /* Apply white only to titles and labels */
    h1, h2, h3, h4, h5, h6, label {{
        color: white !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


set_background("app/background_fraud.jpg")  # put the image name that is in the app folder

# ======== CONTINUE YOUR NORMAL APP BELOW ========

# Load the model, scaler, and selected features
model_data = joblib.load('app/fraud_rf_model.pkl')
model = model_data['model']
scaler = model_data['scaler']
selected_features = model_data['selected_features']

# Function to make predictions
def predict(input_data):
    input_df = pd.DataFrame([input_data])
    input_df[['Amount']] = scaler.transform(input_df[['Amount']])
    prediction = model.predict(input_df[selected_features])
    return prediction[0]

# Function to randomly select a row from the dataset
def get_random_input(data):
    return data.sample(n=1).iloc[0].to_dict()

# Initialize session state variables
if 'input_values' not in st.session_state:
    test_fraud_yes = pd.read_excel('app/test_fraud_yes.xlsx')
    st.session_state.input_values = get_random_input(test_fraud_yes)

if 'run_prediction' not in st.session_state:
    st.session_state.run_prediction = False

# Load test examples
test_fraud_yes = pd.read_excel('app/test_fraud_yes.xlsx')
test_fraud_no = pd.read_excel('app/test_fraud_no.xlsx')

# App title
st.title("Credit Card Fraud Detection \U0001F6A8")

# User inputs for all features, organized in 3 columns
input_data = {feature: 0.0 for feature in selected_features}
cols = st.columns(3)
for i, feature in enumerate(selected_features):
    with cols[i % 3]:
        input_data[feature] = st.number_input(feature, value=float(st.session_state.input_values.get(feature, 0.0)), format="%.6f")

# Side-by-side buttons
button_cols = st.columns(3)

def update_input_values(entities):
    entry = get_random_input(entities)
    entry_df = pd.DataFrame([entry])
    
    # Update values in session_state
    st.session_state.input_values = entry_df.iloc[0].to_dict()
    st.session_state.run_prediction = True
    st.rerun()


with button_cols[0]:
    if st.button("Test with Fraud Data"):
        update_input_values(test_fraud_yes)

with button_cols[1]:
    if st.button("Test with Non-Fraud Data"):
        update_input_values(test_fraud_no)

with button_cols[2]:
    if st.button("Predict"):
        st.session_state.run_prediction = True

# Run prediction
if st.session_state.run_prediction:
    for feature in selected_features:
        input_data[feature] = float(st.session_state.input_values.get(feature, input_data.get(feature, 0.0)))

    prediction = predict(input_data)
    if prediction == 1:
        st.markdown('<p style="color: white;">⚠️ Fraud detected!</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color: white;">✅ No fraud detected.</p>', unsafe_allow_html=True)

    st.session_state.run_prediction = False
