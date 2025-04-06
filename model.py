import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Function to train the model
def train_model(data_path):
   
    # Load the dataset
    data = pd.read_csv(data_path)

    # Assume the dataset has features in columns 'feature1', 'feature2', ..., 'featureN'
    # and the target variable in the column 'behavior' (e.g., 0 for "Safe", 1 for "Unsafe").
    X = data.drop(columns=['behavior'])  # Features
    y = data['behavior']  # Target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy

# Function to predict driver behavior
def predict_behavior(model, features):
    features = np.array(features).reshape(1, -1)  # Reshape for a single prediction
    prediction = model.predict(features)
    return prediction[0]

# Example usage
if __name__ == "__main__":
    # Path to the dataset (replace with your actual dataset path)
    dataset_path = "driver_behavior_data.csv"

    # Train the model
    model, acc = train_model(dataset_path)
    print(f"Model trained with accuracy: {acc * 100:.2f}%")

    # Example prediction
    example_features = [0.5, 1.2, 3.4, 0.8]  # Replace with actual feature values
    prediction = predict_behavior(model, example_features)
    print(f"Predicted behavior: {'Safe' if prediction == 0 else 'Unsafe'}")