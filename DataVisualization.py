import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the file path
file_path = "CICIDS2017.csv"

# STEP 1: COUNT UNIQUE LABELS AND PROTOCOLS
print("\n📌 STEP 1: COUNTING UNIQUE LABELS AND PROTOCOLS:")

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

# STEP 2: BAR CHART FOR LABEL DISTRIBUTION
print("\n📌 STEP 2: VISUALIZING LABEL DISTRIBUTION:")
plt.figure(figsize=(15, 8))  # Large figure for full screen
labels = list(label_counts.keys())
counts = list(label_counts.values())

# Sorting labels by count for better visualization
sorted_indices = sorted(range(len(counts)), key=lambda k: counts[k], reverse=True)
labels = [labels[i] for i in sorted_indices]
counts = [counts[i] for i in sorted_indices]

# Generate different colors
colors = plt.cm.tab10(np.linspace(0, 1, len(labels)))

plt.bar(labels, counts, color=colors, edgecolor="black")
plt.xlabel("LABELS", fontsize=14)
plt.ylabel("COUNT", fontsize=14)
plt.title("LABEL DISTRIBUTION", fontsize=16)
plt.xticks(rotation=45, ha="right", fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Add count labels on top of bars
for i, v in enumerate(counts):
    plt.text(i, v + max(counts) * 0.01, f"{v:,}", ha="center", fontsize=12, fontweight="bold")

# Adjust subplot parameters
plt.subplots_adjust(left=0.082, bottom=0.265, right=0.956, top=0.93)

# Show fullscreen plot
plt.show()

# STEP 3: PIE CHART FOR PROTOCOL DISTRIBUTION
print("\n📌 STEP 3: VISUALIZING PROTOCOL DISTRIBUTION:")
if protocol_counts:  # Check if protocol_counts is not empty
    plt.figure(figsize=(8, 8))
    protocols = list(protocol_counts.keys())
    protocol_values = list(protocol_counts.values())

    plt.pie(
        protocol_values,
        labels=protocols,
        autopct="%1.1f%%",
        colors=plt.cm.Paired(np.linspace(0, 1, len(protocols))),
        startangle=140,
        wedgeprops={"edgecolor": "black"},
        textprops={"fontsize": 10},
    )

    plt.title("PROTOCOL DISTRIBUTION", fontsize=14)
    plt.show()
else:
    print("\n⚠️ No protocol data found for pie chart!")

print("\n✅ DATA VISUALIZATION COMPLETED!")
