import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: LOAD CLEANED DATASET
print("\n📌 STEP 1: LOADING CLEANED DATASET")
file_path = "CICIDS2017_CLEANED.csv"
df = pd.read_csv(file_path)

# STEP 2: FILTER ANOMALIES (LABEL = 1)
print("\n📌 STEP 2: FILTERING ANOMALIES")
anomalies = df[df["LABEL"] == 1]

# STEP 3: COUNT ANOMALIES PER PROTOCOL
print("\n📌 STEP 3: COUNTING ANOMALIES PER PROTOCOL")
protocol_anomalies = anomalies["PROTOCOL"].value_counts()

# MAP PROTOCOL NUMBERS TO NAMES
protocol_mapping = {0: "TCP", 1: "UDP", -1: "Other"}
protocol_anomalies.index = protocol_anomalies.index.map(protocol_mapping)

# DEFINE VIBRANT COLORS
colors = ["#FF6F61", "#6B5B95", "#88B04B"]  # Coral Red, Deep Purple, Vibrant Green

# STEP 4: BAR CHART - PROTOCOL-WISE ANOMALY COUNT
print("\n📌 STEP 4: PLOTTING BAR CHART")
plt.figure(figsize=(10, 6))
plt.bar(protocol_anomalies.index, protocol_anomalies.values, color=colors, edgecolor="black")
plt.xlabel("PROTOCOL", fontsize=12)
plt.ylabel("ANOMALY COUNT", fontsize=12)
plt.title("📊 PROTOCOL-WISE ANOMALY DISTRIBUTION", fontsize=14)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# ADD COUNT LABELS ON BARS
for i, v in enumerate(protocol_anomalies.values):
    plt.text(i, v + max(protocol_anomalies.values) * 0.01, f"{v:,}", ha="center", fontsize=12, fontweight="bold")

plt.show()

# DEFINE COLORS FOR PIE CHART
colors = ["#88B04B", "#FF6F61", "#6B5B95"]  # Vibrant Green, Coral Red, Deep Purple

# STEP 5: PIE CHART - PROTOCOL-WISE ANOMALY PERCENTAGE
print("\n📌 STEP 5: PLOTTING PIE CHART")
plt.figure(figsize=(8, 8))
plt.pie(protocol_anomalies, labels=protocol_anomalies.index, autopct="%1.1f%%", colors=colors, startangle=140, 
        wedgeprops={"edgecolor": "black"}, textprops={"fontsize": 10})
plt.title("📊 PROTOCOL-WISE ANOMALY PERCENTAGE", fontsize=14)
plt.show()

print("\n✅ DATA VISUALIZATION COMPLETED!")
