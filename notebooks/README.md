# Notebooks Folder – Model Development and Testing

This folder contains the full machine learning development process for detecting credit card fraud. It includes exploratory data analysis, model training, evaluation, and creation of testing datasets.

## Contents

- `fraud_project_notebook.ipynb`: Main Jupyter Notebook detailing the full ML workflow:
  - Exploratory Data Analysis (EDA)
  - Feature Engineering
  - Model comparison
  - Final pipeline creation
- `fraud_project.py`: Script version of the notebook for faster execution and exporting the model pipeline as `fraud_rf_model.pkl`.
- `fraud_test_datasets.ipynb`: Notebook used to filter and generate testing datasets for app evaluation:
  - `test_fraud_yes.xlsx`
  - `test_fraud_no.xlsx`
- `util_functions.py`: Python file containing helper functions for cleaning, preprocessing, and model building.

## How to Use

1. **Download the Dataset**  
   - First, download the dataset from [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
   - Place the downloaded `creditcard.csv` file in the same folder as the notebooks.

2. **Run the Notebooks**  
   - Open and run the notebooks in your preferred environment (JupyterLab, VSCode, Google Colab, etc).
   - Ensure all required Python packages are installed (e.g., `pandas`, `scikit-learn`, `matplotlib`, etc).