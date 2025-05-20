# Credit Card Fraud Detection Project

<img align="center" alt="Fraud Detection" width="400" src="https://d27p8o2qkwv41j.cloudfront.net/wp-content/uploads/2017/02/Fraud-Alert-e1487228293461.jpg">

# Overview
This end-to-end project aims to detect fraudulent credit card transactions using machine learning. It includes exploratory data analysis, data preprocessing, model training and evaluation, app development with Streamlit, containerization with Docker, and deployment on Google Cloud Platform (GCP).

🔗 **Live App**: [Access the Fraud Detection App](https://fraud-detection-app-855024627767.us-central1.run.app/)

**Link to Dataset**: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

# About Dataset

### Context
It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.

### Content
The dataset contains transactions made by credit cards in September 2013 by European cardholders.
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data.

# How to Use the App

1. **Adjust the Input Settings**  
   Use the sidebar to fill in customer data, such as **tenure**, **monthly charges**, **internet services**, and **contract type**.

2. **Predict**  
   - Click **Predict** to generate a churn prediction based on the current input values.  
   - The result will indicate whether the customer is likely to **churn** or **stay**, along with the **probability**.

3. **Test with Churn Data**  
   - Click **Test with Churn Data** to auto-fill the form with a real example of a customer who **left**.  
   - The app will automatically run a prediction using this example.

4. **Test with Non-Churn Data**  
   - Click **Test with Non-Churn Data** to auto-fill the form with a real example of a customer who **did not churn**.  
   - The app will show the prediction result accordingly.

# Repository Files
- **app/**: Contains the application files.

- **notebooks/**: Contains the Jupyter notebooks and related scripts.

- **Dockerfile**: Configuration for building the Docker container.

- **requirements.txt**: List of required Python packages.

- **.gitignore**: Git ignored files.

- **README.md**: Project documentation.

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

# How to Use Locally
- Clone the repository to your local machine
- Install dependencies
- Run the Streamlit app

# GCP Deployment
This project was successfully deployed on Google Cloud Platform (GCP) using a Docker container as a study of end-to-end machine learning deployment.

# Author
Julio Cesar Yamashita Martins

# E-mail
yamashitajulio@gmail.com