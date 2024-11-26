#AI-Powered Intrusion Detection System for IoT

This project is an advanced IoT network monitoring system that detects malicious activities in real-time using a trained Random Forest machine learning model and visualizes results on a web-based dashboard powered by Flask. It includes a traffic simulator (`iot_traffic_sim.py`) to generate realistic IoT network data, a training script (`train_model.py`) to build and save the ML model, and a Flask app (`app.py`) to serve a dashboard and REST API for predictions. The system logs data into an SQLite database, processes it using Pandas, and classifies traffic as "Normal" or "Malicious" with Scikit-learn. The dashboard, styled with HTML and CSS, displays recent traffic logs and predictions, while the API provides programmatic access to the latest detection results. Users can clone the repository, install dependencies from `requirements.txt`, simulate traffic, train the model, and access the system at `http://127.0.0.1:5000`. Designed for IoT security enthusiasts, this project demonstrates expertise in Python, Flask, machine learning, and cybersecurity. 

---

## Installation and Usage
1. Clone the repository: `git clone https://github.com/priyanshijuyal/IDS-for-IoT.git`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Simulate traffic: `python iot_traffic_sim.py`.
4. Train the model: `python train_model.py`.
5. Run the Flask app: `python app.py` and access at `http://127.0.0.1:5000`.

---

## Contact
For questions or suggestions, contact:
**Name**: Priyanshi 
**Email**: priyanshijuyal.75@gmail.com  
**GitHub**:(https://github.com/priyanshijuyal)

