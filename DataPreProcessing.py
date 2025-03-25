import pandas as pd  

# SET FILE PATHS
input_file = "CICIDS2017.csv"
output_file = "CICIDS2017_CLEANED.csv"

# STEP 1: LOAD A SAMPLE TO IDENTIFY COLUMN NAMES
print("\n📌 STEP 1: LOADING A SAMPLE TO CHECK COLUMN STRUCTURE:")
df_sample = pd.read_csv(input_file, nrows=100)

# IDENTIFY PAYLOAD COLUMNS
payload_cols = [col for col in df_sample.columns if col.startswith("payload_byte_")]
selected_cols = [col for col in df_sample.columns if col not in payload_cols]

print("🔹 Total Columns in Sample:", len(df_sample.columns))
print("🔹 Selected Columns (Excluding Payload):", len(selected_cols))
print("🔹 First 5 Columns:", selected_cols[:5])

# STEP 2: LOAD DATASET WITHOUT PAYLOAD COLUMNS & PROCESS IN CHUNKS
print("\n📌 STEP 2: PROCESSING DATA IN CHUNKS:")
chunk_size = 50000  
processed_chunks = []

for chunk in pd.read_csv(input_file, usecols=selected_cols, chunksize=chunk_size):
    print(f"🚀 Processing Chunk of {len(chunk)} Rows...")
    
    # CONVERT COLUMN NAMES TO UPPERCASE
    chunk.columns = [col.upper() for col in chunk.columns]
    
    # CONVERT 'LABEL' COLUMN (BENIGN → 0, ATTACK → 1)
    chunk["LABEL"] = chunk["LABEL"].apply(lambda x: 0 if x == "BENIGN" else 1)
    
    # CONVERT 'PROTOCOL' COLUMN (TCP → 0, UDP → 1, OTHERS → -1)
    chunk["PROTOCOL"] = chunk["PROTOCOL"].map({"tcp": 0, "udp": 1}).fillna(-1).astype(int)
    
    processed_chunks.append(chunk)
    print("✅ Chunk Processed Successfully!")

# STEP 3: COMBINE ALL CHUNKS & SAVE CLEANED DATA
print("\n📌 STEP 3: SAVING CLEANED DATASET:")
df_cleaned = pd.concat(processed_chunks, ignore_index=True)
df_cleaned.to_csv(output_file, index=False)

print("\n✅ DATA PREPROCESSING COMPLETED!")
print(f"💾 CLEANED DATASET SAVED AS: {output_file}")
