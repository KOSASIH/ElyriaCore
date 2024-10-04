import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load training data
train_data = pd.read_csv('training_data.csv')

# Preprocess data
X = train_data.drop(['disease'], axis=1)
y = train_data['disease']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Use the model to make predictions on new data
def diagnose_disease(symptoms):
    symptoms_df = pd.DataFrame([symptoms], columns=X.columns)
    prediction = clf.predict(symptoms_df)
    return prediction[0]

# Example usage:
symptoms = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
disease = diagnose_disease(symptoms)
print('Predicted disease:', disease)
