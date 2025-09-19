from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for all routes (during development)
CORS(app)

@app.route('/')
def index():
    return jsonify({"Choo Choo2": "Welcome to your Flask app 🚅"})

@app.route('/api/moisture')
def moisture():
    # Example fake data (replace with DB query later)
    return jsonify({"sensor_id": 1, "moisture": 42, "unit": "%", "timestamp": "2025-09-09T12:00:00Z"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
