# Credit Card Fraud Detection Project

<img align="center" alt="Fraud Detection" width="400" src="https://d27p8o2qkwv41j.cloudfront.net/wp-content/uploads/2017/02/Fraud-Alert-e1487228293461.jpg">

# Overview
This end-to-end project aims to detect fraudulent credit card transactions using machine learning. It includes exploratory data analysis, data preprocessing, model training and evaluation, app development with Streamlit, containerization with Docker, and deployment on Google Cloud Platform (GCP).

🔗 **Live App**: [Access the Fraud Detection App](https://fraud-detection-app-855024627767.us-central1.run.app/)

Link to Dataset: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

# Required Libraries
The following Python packages are required to run this project:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- streamlit
- openpyxl
- joblib

# Repository Files
- **app/**: Contains the application files:
  - `fraud_app.py`: Streamlit app to input variables and return predictions.
  - `fraud_rf_model.pkl`: Serialized pipeline and trained model.
  - `background_fraud.jpg`: Background image used in the app.
  - `test_fraud_yes.xlsx`: Sample of fraudulent transactions for testing.
  - `test_fraud_no.xlsx`: Sample of non-fraudulent transactions for testing.

- **notebooks/**: Contains the Jupyter notebooks and related scripts:
  - `fraud_project_notebook.ipynb`: Complete analysis and model development process.
  - `fraud_project.py`: Script for training the model and saving the pipeline.
  - `fraud_test_datasets.ipynb`: Creates testing datasets used in the app.
  - `util_functions.py`: Helper functions used in the project.

- **Dockerfile**: Configuration for building the Docker container.

- **requirements.txt**: List of required Python packages.

- **.gitignore**: Git ignored files.

- **README.md**: Project documentation.

# How to Use Locally
- Clone the repository to your local machine
- Install dependencies
- Run the Streamlit app

Use the provided test files (test_fraud_yes.xlsx and test_fraud_no.xlsx) to quickly evaluate the model behavior.

# Docker Usage
To run the app using Docker:

bash
Copiar
Editar
docker build -t fraud-app .
docker run -p 8501:8501 fraud-app

# GCP Deployment
This project was successfully deployed on Google Cloud Platform (GCP) using a Docker container as a study of end-to-end machine learning deployment.

# Author
Julio Cesar Yamashita Martins

# E-mail
yamashitajulio@gmail.com