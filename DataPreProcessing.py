import pandas as pd  

# Set file paths (Update as needed)
input_file = "CICIDS2017.csv"
output_file = "CICIDS2017_CLEANED.csv"

# Step 1: Load a sample to identify column names
df_sample = pd.read_csv(input_file, nrows=100)
payload_cols = [col for col in df_sample.columns if col.startswith("payload_byte_")]
selected_cols = [col for col in df_sample.columns if col not in payload_cols]

# Step 2: Load dataset without payload columns in chunks and process
chunk_size = 50000  
processed_chunks = []

for chunk in pd.read_csv(input_file, usecols=selected_cols, chunksize=chunk_size):
    # Convert column names to uppercase
    chunk.columns = [col.upper() for col in chunk.columns]

    # Convert 'LABEL' column (BENIGN → 0, Attack → 1)
    chunk["LABEL"] = chunk["LABEL"].apply(lambda x: 0 if x == "BENIGN" else 1)

    # Convert 'PROTOCOL' column (TCP → 0, UDP → 1, others → -1)
    chunk["PROTOCOL"] = chunk["PROTOCOL"].map({"tcp": 0, "udp": 1}).fillna(-1).astype(int)

    processed_chunks.append(chunk)

# Step 3: Combine all chunks and save
df_cleaned = pd.concat(processed_chunks, ignore_index=True)
df_cleaned.to_csv(output_file, index=False)

print("\n✅ Data Preprocessing Completed!")
print(f"💾 Cleaned Dataset saved as: {output_file}")
