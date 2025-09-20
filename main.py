from flask import Flask, jsonify, request
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

@app.route("/api/moisture", methods=["POST"])
def get_moisture():
    #now = datetime.datetime.utcnow()
    data = request.json
    #sensor_id = data.get("sensor_id")
    #moisture = data.get("moisture")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
