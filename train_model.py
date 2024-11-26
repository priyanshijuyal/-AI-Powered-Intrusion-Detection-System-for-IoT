import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Database connection
conn = sqlite3.connect("database/ids_data.db")
query = "SELECT * FROM traffic"
df = pd.read_sql_query(query, conn)

# Preprocessing
df["is_malicious"] = df["traffic_type"].apply(lambda x: 1 if x == "Malicious" else 0)
X = pd.get_dummies(df[["source_ip", "dest_ip", "protocol"]])
y = df["is_malicious"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate and save model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
joblib.dump(model, "models/ids_model.pkl")
print("Model saved to models/ids_model.pkl")
