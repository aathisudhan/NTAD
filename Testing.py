import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib  # for loading the trained model

# STEP 1: LOAD CAPTURED DATA
print("\n📌 STEP 1: LOADING CAPTURED DATA")
new_data = pd.read_csv('normalized_real_time_data.csv')  # Replace with actual data file

# STEP 2: LOAD TRAINED ISOLATION FOREST MODEL
print("\n📌 STEP 2: LOADING TRAINED MODEL")
model = joblib.load('isolation_forest_model.pkl')

# STEP 3: MAKE PREDICTIONS
print("\n📌 STEP 3: PREDICTING ANOMALIES")
predictions = model.predict(new_data)

# Convert predictions (-1 for outliers, 1 for inliers) to 0 (anomaly) and 1 (benign)
predictions = [1 if pred == 1 else 0 for pred in predictions]

# STEP 4: DISPLAY RESULTS
print("\n📌 STEP 4: DISPLAYING RESULTS")
print("Predictions:", predictions)

# Optionally, check how many anomalies were detected
num_anomalies = sum(1 for pred in predictions if pred == 1)
print(f"Number of anomalies detected: {num_anomalies}")

print("\n✅ ANOMALY DETECTION COMPLETED!")
