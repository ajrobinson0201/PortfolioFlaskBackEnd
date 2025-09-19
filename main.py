from flask import Flask, jsonify
from flask_cors import CORS
import os
import datetime
import random

app = Flask(__name__)

# Enable CORS for all routes (during development)
CORS(app)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route("/api/moisture")
def get_moisture():
    now = datetime.datetime.utcnow()
    fake_data = [
        {
            "timestamp": (now - datetime.timedelta(minutes=i)).isoformat(),
            "sensor_id": 1,
            "moisture": round(random.uniform(25.0, 40.0), 2)
        }
        for i in range(10)
    ]
    return jsonify(fake_data)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
