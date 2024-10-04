import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load training data
train_data = pd.read_csv('training_data.csv')

# Preprocess data
X = train_data.drop(['treatment_outcome'], axis=1)
y = train_data['treatment_outcome']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a random forest regressor
clf = RandomForestRegressor(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squared Error:', mse)
print('R-Squared:', r2)

# Use the model to make predictions on new data
def plan_treatment(patient_data):
    patient_df = pd.DataFrame([patient_data], columns=X.columns)
    prediction = clf.predict(patient_df)
    return prediction[0]

# Example usage:
patient_data = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
treatment_outcome = plan_treatment(patient_data)
print('Predicted treatment outcome:', treatment_outcome)

# Use the model to optimize treatment plans
def optimize_treatment_plan(patient_data, treatment_options):
    treatment_outcomes = []
    for treatment in treatment_options:
        patient_data_with_treatment = patient_data + [treatment]
        treatment_outcome = plan_treatment(patient_data_with_treatment)
        treatment_outcomes.append(treatment_outcome)
    best_treatment = treatment_options[np.argmax(treatment_outcomes)]
    return best_treatment

# Example usage:
patient_data = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
treatment_options = [1, 2, 3]
best_treatment = optimize_treatment_plan(patient_data, treatment_options)
print('Best treatment:', best_treatment)
