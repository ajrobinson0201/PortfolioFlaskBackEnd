from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import datetime

app = Flask(__name__)

# Enable CORS for all routes (during development)
CORS(app)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

readings = []
@app.route("/api/moisture", methods=["POST"])
def post_moisture():
    now = datetime.datetime.utcnow()
    data = request.json
    sensor_id = data.get("sensor_id")
    moisture = data.get("moisture")

    readings.append({
        "sensor_id": sensor_id,
        "moisture": moisture,
        "timestamp": now
    })
    return jsonify({"status": "ok"}), 200

@app.route("/api/moisture", methods=["GET"])
def get_moisture():
    # In production: query DB
    return jsonify(readings[-50:])

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
