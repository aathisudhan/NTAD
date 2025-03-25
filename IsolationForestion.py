import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, 
    classification_report, confusion_matrix
)
import joblib

# 📌 STEP 1: LOAD DATA
print("\n📌 STEP 1: LOADING DATA:")
X_train = pd.read_csv("X_TRAIN.csv")
X_valid = pd.read_csv("X_VALID.csv")
Y_train = pd.read_csv("Y_TRAIN.csv").squeeze()
Y_valid = pd.read_csv("Y_VALID.csv").squeeze()

print("🔹 Training Data Shape:", X_train.shape)
print("🔹 Validation Data Shape:", X_valid.shape)

# ✅ STEP 2: TRAIN ISOLATION FOREST MODEL
print("\n📌 STEP 2: TRAINING ISOLATION FOREST MODEL:")
model = IsolationForest(max_samples=256, n_estimators=150, contamination=0.25, random_state=42)
model.fit(X_train)
print("✅ Model Training Completed!")

# 📌 STEP 3: PREDICT ANOMALIES
print("\n📌 STEP 3: PREDICTING ANOMALIES:")
y_pred = model.predict(X_valid)
y_pred = np.where(y_pred == 1, 1, 0)  # Convert -1 (anomaly) to 0, 1 (benign) remains 1
print("✅ Predictions Completed!")

# ✅ STEP 4: COMPUTE EVALUATION METRICS
print("\n📌 STEP 4: COMPUTING EVALUATION METRICS:")
accuracy = accuracy_score(Y_valid, y_pred)
precision = precision_score(Y_valid, y_pred)
recall = recall_score(Y_valid, y_pred)
f1 = f1_score(Y_valid, y_pred)
roc_auc = roc_auc_score(Y_valid, y_pred)
misclassification_rate = 100 - (accuracy * 100)  # Misclassification Rate

print("✅ Classification Report:\n", classification_report(Y_valid, y_pred))
print("✅ Confusion Matrix:\n", confusion_matrix(Y_valid, y_pred))
print(f"✅ Accuracy: {accuracy:.2f}")
print(f"✅ Precision: {precision:.2f}")
print(f"✅ Recall: {recall:.2f}")
print(f"✅ F1 Score: {f1:.2f}")
print(f"✅ ROC-AUC Score: {roc_auc:.2f}")
print(f"✅ Misclassification Rate: {misclassification_rate:.2f}%")

# 📌 STEP 5: SAVE THE MODEL
print("\n📌 STEP 5: SAVING THE MODEL:")
joblib.dump(model, "isolation_forest_model.pkl")
print("✅ Model saved successfully!")

# 📊 STEP 6: VISUALIZE METRICS
print("\n📌 STEP 6: VISUALIZING RESULTS:")

# Plot Accuracy & Misclassification Rate
metrics = ["ACCURACY", "MISCLASSIFICATION RATE"]
values = [accuracy * 100, misclassification_rate]
plt.figure(figsize=(6, 4))
plt.bar(metrics, values, color=["royalblue", "crimson"], edgecolor="black")
plt.ylabel("PERCENTAGE")
plt.title("MODEL ACCURACY & ERROR RATE")
plt.ylim(0, 100)
for i, v in enumerate(values):
    plt.text(i, v + 2, f"{v:.2f}%", ha="center", fontsize=12, fontweight="bold")
plt.show()

# Plot Confusion Matrix
plt.figure(figsize=(6, 5))
sns.heatmap(confusion_matrix(Y_valid, y_pred), annot=True, fmt="d", cmap="coolwarm", 
            xticklabels=["Anomaly", "Benign"], yticklabels=["Anomaly", "Benign"])
plt.xlabel("PREDICTED LABEL")
plt.ylabel("TRUE LABEL")
plt.title("CONFUSION MATRIX")
plt.show()

# Plot ROC Curve
fpr, tpr, _ = roc_curve(Y_valid, y_pred)
plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})", color="darkorange")
plt.plot([0, 1], [0, 1], "k--")  # Diagonal reference line
plt.xlabel("FALSE POSITIVE RATE")
plt.ylabel("TRUE POSITIVE RATE")
plt.title("ROC CURVE")
plt.legend()
plt.show()

print("\n✅ DATA ANALYSIS COMPLETED!")
