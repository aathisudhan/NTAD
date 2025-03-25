from scapy.all import sniff, IP, TCP, UDP
import pandas as pd

# STEP 1: INITIALIZE DATA COLLECTION
print("\n\ud83d\udccc STEP 1: INITIALIZING PACKET CAPTURE")
# List to store captured data
data_list = []

def packet_callback(packet):
    if IP in packet:
        # Check if the packet is TCP or UDP and assign 0 or 1 accordingly
        if TCP in packet:
            protocol = 0  # TCP
        elif UDP in packet:
            protocol = 1  # UDP
        else:
            protocol = -1  # Unknown or other protocol

        data_list.append({
            "TTL": packet[IP].ttl,
            "TOTAL_LEN": len(packet),
            "PROTOCOL": protocol,  # Use 0 for TCP and 1 for UDP
            "T_DELTA": packet.time  # You may need to compute the difference
        })

# STEP 2: START PACKET CAPTURE
print("\n\ud83d\udccc STEP 2: CAPTURING NETWORK PACKETS")
# Capture packets (adjust count or timeout as needed)
sniff(prn=packet_callback, count=200)

# STEP 3: SAVE DATA TO CSV
print("\n\ud83d\udccc STEP 3: SAVING CAPTURED DATA")
# Convert to DataFrame
df = pd.DataFrame(data_list)
df.to_csv("captured_network_data.csv", index=False)

print("\n✅ NETWORK DATA CAPTURED AND SAVED!")
