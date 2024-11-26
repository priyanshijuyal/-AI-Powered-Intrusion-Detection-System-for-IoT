import time
import random
import sqlite3

# Database setup
conn = sqlite3.connect("database/ids_data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS traffic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_ip TEXT,
    dest_ip TEXT,
    protocol TEXT,
    traffic_type TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Traffic simulation function
def generate_traffic():
    source_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    dest_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
    protocols = ["HTTP", "HTTPS", "FTP", "SSH"]
    traffic_types = ["Normal", "Malicious"]

    while True:
        traffic_data = {
            "source_ip": random.choice(source_ips),
            "dest_ip": random.choice(dest_ips),
            "protocol": random.choice(protocols),
            "traffic_type": random.choices(traffic_types, weights=[80, 20])[0],
        }
        cursor.execute("""
        INSERT INTO traffic (source_ip, dest_ip, protocol, traffic_type)
        VALUES (:source_ip, :dest_ip, :protocol, :traffic_type)
        """, traffic_data)
        conn.commit()

        print(f"Generated Traffic: {traffic_data}")
        time.sleep(1)

if __name__ == "__main__":
    try:
        generate_traffic()
    except KeyboardInterrupt:
        print("Traffic simulation stopped.")
