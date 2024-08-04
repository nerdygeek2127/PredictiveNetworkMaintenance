import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Path to the Excel file
file_path = r"C:\Users\lohit\Desktop\EVENG\Pyhton scripts\enlighted dongle\ML\Data.xlsx"

# Manually specify the column names
column_names = [
    'Timestamp', 'CPU Usage (%)', 'Memory Usage (%)', 'Disk I/O (ops/sec)',
    'Network Latency (ms)', 'Network Throughput (Mbps)', 'Error Rate'
]

# Read data from Excel file, skipping the first 4 rows which are empty or headers
data = pd.read_excel(file_path, skiprows=4, names=column_names)

# Strip any leading/trailing whitespace characters from the column names
data.columns = data.columns.str.strip()

# Print the column names to verify them
print("Column names:", data.columns)

# Print the first few rows to verify
print("First few rows of the dataset:")
print(data.head())

# Generate 'Maintenance Needed (0/1)' column based on a condition
# Maintenance needed if CPU usage > 80% or Memory usage > 90%
data['Maintenance Needed (0/1)'] = ((data['CPU Usage (%)'] > 80) | (data['Memory Usage (%)'] > 90)).astype(int)

# Data Preprocessing
# Dropping the 'Timestamp' column and separating features and target
features = data.drop(['Timestamp', 'Maintenance Needed (0/1)'], axis=1)
target = data['Maintenance Needed (0/1)']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Model Training
# Creating and training the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
# Making predictions on the testing set
y_pred = model.predict(X_test)

# Evaluating the model
print("Accuracy:", accuracy_score(y_test, y_pred))

# Making Predictions on the entire dataset
data['Predicted Maintenance Needed (0/1)'] = model.predict(features)

# Print the entire dataset with predictions
print("Full dataset with predictions:")
print(data)

# Save the DataFrame to a new Excel file
output_file_path = r"C:\Users\lohit\Desktop\EVENG\Pyhton scripts\enlighted dongle\ML\Output_Data_New.xlsx"
data.to_excel(output_file_path, index=False)
print(f"Output saved to {output_file_path}")
