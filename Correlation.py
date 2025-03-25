import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# STEP 1: LOAD TRAINING AND VALIDATION DATA
print("\n📌 STEP 1: LOADING DATASET")
X_train = pd.read_csv("X_TRAIN.csv")
X_valid = pd.read_csv("X_VALID.csv")

# DISPLAY DATASET SHAPE
print("\n🚀 DATASET SHAPE:")
print("🔹 Training Set Shape:", X_train.shape)
print("🔹 Validation Set Shape:", X_valid.shape)

# STEP 2: COMPUTE CORRELATION MATRIX
print("\n📌 STEP 2: COMPUTING CORRELATION MATRIX")
corr_matrix = X_train.corr()

# STEP 3: VISUALIZE CORRELATION MATRIX
print("\n📌 STEP 3: PLOTTING CORRELATION MATRIX")
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('✨ CORRELATION MATRIX')
plt.show()

# STEP 4: IDENTIFY HIGHLY CORRELATED FEATURES
print("\n📌 STEP 4: IDENTIFYING HIGHLY CORRELATED FEATURES")
threshold = 0.95  # Define correlation threshold
upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Extract features with high correlation
highly_correlated_features = [column for column in upper_triangle.columns if any(upper_triangle[column] > threshold)]

print("\n🛠️ Highly Correlated Features (above 0.95):", highly_correlated_features)

# STEP 5: REMOVE HIGHLY CORRELATED FEATURES
print("\n📌 STEP 5: REDUCING DATASET")
X_train_reduced = X_train.drop(columns=highly_correlated_features)
X_valid_reduced = X_valid.drop(columns=highly_correlated_features)

# DISPLAY NEW DATASET SHAPE
print("\n🛠️ DATASET SHAPE AFTER REMOVAL:")
print("🔹 Original Training Shape:", X_train.shape)
print("🔹 Reduced Training Shape:", X_train_reduced.shape)

print("\n✅ DATA PROCESSING COMPLETED!")
