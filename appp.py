from sklearn.compose import ColumnTransformer

# Load preprocessor and model
preprocessor = joblib.load("models/preprocessor.pkl")
model = joblib.load("models/ids_model.pkl")

@app.route("/api/detect", methods=["GET"])
def detect():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM traffic ORDER BY timestamp DESC LIMIT 1")
    latest_traffic = cursor.fetchone()

    if latest_traffic:
        # Prepare data
        df = pd.DataFrame([latest_traffic[1:4]], columns=["source_ip", "dest_ip", "protocol"])
        df_transformed = preprocessor.transform(df)
        
        # Predict
        prediction = model.predict(df_transformed)
        result = "Malicious" if prediction[0] == 1 else "Normal"
        return jsonify({"result": result, "data": latest_traffic})

    return jsonify({"error": "No traffic data available"})

