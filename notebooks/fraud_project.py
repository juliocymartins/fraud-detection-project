import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import classification_report

# Supress warnings
import warnings
warnings.filterwarnings("ignore")

# Load dataset
fraud_df_clean = pd.read_csv('creditcard.csv')

# Drop the 'Time' feature
fraud_df_clean = fraud_df_clean.drop(columns=['Time'])

# Split the dataset
X = fraud_df_clean.drop(columns=['Class'])
y = fraud_df_clean['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Scale the 'Amount' feature
scaler = StandardScaler()
X_train[['Amount']] = scaler.fit_transform(X_train[['Amount']])
X_test[['Amount']] = scaler.transform(X_test[['Amount']])

# Apply SMOTE for oversampling
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Initialize and train the model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train_smote, y_train_smote)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Print the classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the trained model, scaler, and the selected features
selected_features = fraud_df_clean.drop(columns=['Class']).columns.tolist()
joblib.dump({'model': rf_model, 'scaler': scaler, 'selected_features': selected_features}, 'fraud_rf_model.pkl')
print("Model, scaler, and selected features saved in fraud_rf_model.pkl")