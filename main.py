"""
The client module which allows simulating and checking sensor data for 
potential anomalies. This is achieved by generating sample data and 
communicating with the server module, which sends back labels predicted by 
the trained model.
"""

import json
import time

from flask import Flask, render_template, request, Response
import numpy as np
import requests
from requests.exceptions import JSONDecodeError

# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def index():
    """Renders the main index page."""
    return render_template('index.html')


@app.route('/check')
def check():
    """Checks the selected sensor and get its data."""
    selected_sensor = request.args.get('sensor')
    if not selected_sensor:
        return 'No sensor selected!'
    return Response(generate(), content_type='text/event-stream')


def generate():
    """Continuously generates and sends sensor data."""
    while True:
        data = generate_sensor_data()
        response = requests.post(
            'http://localhost:8080/predict', json=data, timeout=30000)
        time.sleep(1)

        try:
            json_data = response.json()
            predicted_label = json_data['predicted_label']
        except (JSONDecodeError, KeyError):
            predicted_label = 'Error or Invalid Response'

        data['Label'] = predicted_label
        yield f'data: {json.dumps(data)}\n\n'


def generate_sensor_data():
    """Generates random sensor data."""
    names = ['Temperature', 'Humidity', 'Loudness']
    min_values = [10, 0, 100]
    max_values = [30, 100, 150]
    data = {}

    for i, name in enumerate(names):
        mu = (min_values[i] + max_values[i]) / 2
        sigma = (min_values[i] + max_values[i]) / 6
        data[name] = np.random.normal(mu, sigma)

    return data


if __name__ == '__main__':
    app.run(threaded=True)
