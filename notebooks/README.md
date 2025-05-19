# Notebooks Folder – Model Development and Testing

This folder contains the full machine learning development process for detecting credit card fraud. It includes exploratory data analysis, model training, evaluation, and creation of testing datasets.

## Contents

- `fraud_project_notebook.ipynb`: Main Jupyter Notebook detailing the full ML workflow:
  - Exploratory Data Analysis (EDA)
  - Feature Engineering
  - Model comparison
  - Final pipeline creation
  - Exporting the model with joblib
- `fraud_project.py`: Script version of the notebook for faster execution and exporting the model pipeline as `fraud_rf_model.pkl`.
- `fraud_test_datasets.ipynb`: Notebook used to filter and generate testing datasets for app evaluation:
  - `test_fraud_yes.xlsx`
  - `test_fraud_no.xlsx`
- `util_functions.py`: Python file containing helper functions for cleaning, preprocessing, and model building.

## How to Use

You can open and run the notebooks in your preferred environment (JupyterLab, VSCode, Google Colab, etc). Make sure the dataset is available and the required packages are installed.
