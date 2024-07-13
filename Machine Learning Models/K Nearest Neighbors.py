import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, accuracy_score

# Load the dataset
fire_and_smoke = pd.read_csv("D:/College Work/AI/AI Hackathon/Datasets/smoke_detection_iot.csv")

# Display the first few rows of the dataset
print(fire_and_smoke.head())

# Number of rows and columns
print(fire_and_smoke.shape)

# Descriptive Statistics of the Dataset
print(fire_and_smoke.describe())

# Separate data for fire triggered and not triggered
fire_triggered = fire_and_smoke[fire_and_smoke['Fire Alarm'] == 1]['Temperature[C]']
no_fire_triggered = fire_and_smoke[fire_and_smoke['Fire Alarm'] == 0]['Temperature[C]']
print(fire_triggered)
print(no_fire_triggered)

# Splitting the Dataset into Training and Test Data
X = fire_and_smoke.drop('Fire Alarm', axis=1)  # Features
Y = fire_and_smoke['Fire Alarm']  # Target variable

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# Model Making
knn_model = KNeighborsClassifier(n_neighbors=5)

# Training the KNN model with Training Data
knn_model.fit(X_train, Y_train)

# Accuracy on Training Data
X_train_prediction = knn_model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training Data: ', training_data_accuracy)

# Accuracy on Test Data
X_test_prediction = knn_model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on Testing Data: ', testing_data_accuracy)

# Making Predictions
Y_pred = knn_model.predict(X_test)

# Evaluating the Model
r2 = r2_score(Y_test, Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
accuracy = accuracy_score(Y_test, Y_pred)

print("KNN Model Evaluation:")
print(f"R2 Score: {r2}")
print(f"Mean Absolute Error: {mae}")
print(f"Mean Square Error: {mse}")
print(f"Accuracy: {accuracy}")

# Making a Predictive System
input_data = (1654756905,-20.083,54.03,1417,415,12973,19382,938.733,1.88,1.95,12.94,2.018,0.046,23574)
input_data_as_numpy_array = np.asarray(input_data)

# Convert to DataFrame and ensure the correct feature names
input_data_reshaped = pd.DataFrame(input_data_as_numpy_array.reshape(1, -1), columns=X.columns)

# Make the prediction
prediction = knn_model.predict(input_data_reshaped)

# Output the prediction
if prediction[0] == 1:
    print('There is a Fire, call Emergency')
else:
    print('There is no Fire')