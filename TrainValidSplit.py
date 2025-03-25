import pandas as pd  
from sklearn.model_selection import train_test_split  

# 📌 STEP 1: LOAD CLEANED DATASET
file_path = "CICIDS2017_CLEANED.csv"
print("\n🚀 LOADING CLEANED DATASET:")
df = pd.read_csv(file_path)
print(f"🔹 Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")

# 📌 STEP 2: SEPARATE FEATURES AND TARGET
print("\n🚀 SEPARATING FEATURES (X) AND TARGET (Y):")
X = df.drop(columns=["LABEL"])  # Features
Y = df["LABEL"]  # Target (0 = Benign, 1 = Attack)
print(f"🔹 Features Shape: {X.shape}, Target Shape: {Y.shape}")

# 📌 STEP 3: TRAIN-VALIDATION SPLIT (70% Train, 30% Validation)
print("\n🚀 SPLITTING DATA INTO TRAIN & VALIDATION SETS:")
X_train, X_valid, Y_train, Y_valid = train_test_split(
    X, Y, test_size=0.3, random_state=42, stratify=Y
)

# 📌 STEP 4: SAVE SPLIT DATA (OPTIONAL)
print("\n💾 SAVING SPLIT DATASETS:")
X_train.to_csv("X_TRAIN.csv", index=False)
print(f"✅ X_TRAIN Saved: {X_train.shape}")
X_valid.to_csv("X_VALID.csv", index=False)
print(f"✅ X_VALID Saved: {X_valid.shape}")
Y_train.to_csv("Y_TRAIN.csv", index=False)
print(f"✅ Y_TRAIN Saved: {Y_train.shape}")
Y_valid.to_csv("Y_VALID.csv", index=False)
print(f"✅ Y_VALID Saved: {Y_valid.shape}")

# 📌 FINAL STATUS
print("\n✅ TRAIN-VALIDATION SPLIT COMPLETED SUCCESSFULLY!")
