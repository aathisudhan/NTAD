import pandas as pd

# STEP 1: LOAD DATASETS
print("\n📌 STEP 1: LOADING DATASETS")
# Load the CSV files (replace with actual file paths)
training_data = pd.read_csv('CICIDS2017_CLEANED.csv')  # CSV file with 1.4 million rows
real_time_data = pd.read_csv('captured_network_data.csv')  # CSV file with 100 rows

# STEP 2: CALCULATE MIN & MAX T_DELTA FROM TRAINING DATASET
print("\n📌 STEP 2: CALCULATING MIN-MAX T_DELTA")
min_train_tdelta = training_data['T_DELTA'].min()
max_train_tdelta = training_data['T_DELTA'].max()

# STEP 3: APPLY MIN-MAX SCALING TO REAL-TIME DATA
print("\n📌 STEP 3: NORMALIZING REAL-TIME DATA")
real_time_data['T_DELTA'] = ((real_time_data['T_DELTA'] - min_train_tdelta) / 
                              (max_train_tdelta - min_train_tdelta)) * (max_train_tdelta - min_train_tdelta) + min_train_tdelta

# STEP 4: SAVE NORMALIZED DATA TO CSV
print("\n📌 STEP 4: SAVING NORMALIZED DATA")
real_time_data.to_csv('normalized_real_time_data.csv', index=False)

# STEP 5: INSPECT RESULTS
print("\n📌 STEP 5: DISPLAYING PROCESSED DATA")
print(real_time_data[['TTL', 'TOTAL_LEN', 'PROTOCOL', 'T_DELTA']])

print("\n✅ DATA NORMALIZATION COMPLETED!")
