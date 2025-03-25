import pandas as pd
import matplotlib.pyplot as plt

# Set the file path
file_path = "CICIDS2017.csv"

# STEP 1: LOAD A SAMPLE TO CHECK DATA STRUCTURE
print("\n📌 STEP 1: LOADING A SAMPLE (FIRST 5000 ROWS):")
df_sample = pd.read_csv(file_path, nrows=5000)

# DISPLAY DATASET STRUCTURE
print("\n🚀 DATASET BASIC INFO:")
print("🔹 Total Columns:", df_sample.shape[1])
print("🔹 Column Names:", df_sample.columns.tolist())
print("\n🚀 FIRST 5 ROWS OF THE DATA:")
print(df_sample.head())

# STEP 2: COUNT TOTAL ROWS WITHOUT LOADING FULL DATASET
print("\n📌 STEP 2: COUNTING TOTAL ROWS:")

def count_rows(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for line in f) - 1  # Subtract header

num_rows = count_rows(file_path)
print("\n🔢 Total Number of Rows:", num_rows)

# STEP 3: COUNT UNIQUE VALUES IN 'LABEL' AND 'PROTOCOL'
print("\n📌 STEP 3: COUNTING UNIQUE LABELS AND PROTOCOLS:")

chunk_size = 100000
label_counts = {}
protocol_counts = {}

for chunk in pd.read_csv(file_path, usecols=["label", "protocol"], chunksize=chunk_size):
    # Count labels
    label_chunk_counts = chunk["label"].value_counts().to_dict()
    for label, count in label_chunk_counts.items():
        label_counts[label] = label_counts.get(label, 0) + count

    # Count protocols
    protocol_chunk_counts = chunk["protocol"].value_counts().to_dict()
    for protocol, count in protocol_chunk_counts.items():
        protocol_counts[protocol] = protocol_counts.get(protocol, 0) + count

# PRINT LABEL COUNTS
print("\n🎯 UNIQUE LABELS AND THEIR COUNTS:")
for label, count in label_counts.items():
    print(f"🔹 {label}: {count}")

# PRINT PROTOCOL COUNTS
print("\n🎯 UNIQUE PROTOCOLS AND THEIR COUNTS:")
for protocol, count in protocol_counts.items():
    print(f"🔹 {protocol}: {count}")

# STEP 4: CHECK MISSING VALUES AND DATA TYPES
print("\n📌 STEP 4: CHECKING MISSING VALUES AND DATA TYPES:\n")

df_sample.info()

# IMPROVED MISSING VALUES CHECK
missing_values = df_sample.isnull().sum()
missing_values_alt = (df_sample == "").sum() + (df_sample == " ").sum()
missing_values_total = missing_values + missing_values_alt

print("\n⚠️ COLUMNS WITH MISSING VALUES:")
print(missing_values_total[missing_values_total > 0])

# STEP 5: DISPLAY FIRST 5 ROWS OF LAST 5 COLUMNS
print("\n📌 STEP 5: FIRST 5 ROWS OF THE LAST 5 COLUMNS:\n")
last_5_cols = df_sample.columns[-5:]  # Select last 5 columns
print(df_sample[last_5_cols].head())

print("\n✅ DATA EXPLORATION COMPLETED!")
