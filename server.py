"""
The server module that receives data via POST requests and responds with
proper labels as predicted by the trained model.
"""

import logging
import pickle

from flask import Flask, request, jsonify
from sklearn.exceptions import NotFittedError

logging.basicConfig(level=logging.DEBUG)

MODEL_FILENAME = 'trained_model.pkl'
SCALER_FILENAME = 'scaler.pkl'
FEATURE_NAMES = ['Temperature', 'Humidity', 'Loudness']

app = Flask(__name__)


def load_model(model_filename):
    """Loads the trained model from disk."""
    loaded_model = None
    with open(model_filename, 'rb') as f:
        loaded_model = pickle.load(f)
    return loaded_model


def extract_features(data):
    """Extracts the relevant features from input data."""
    return [data[name] for name in FEATURE_NAMES]


model = load_model(MODEL_FILENAME)


@app.route('/predict', methods=['POST'])
def predict():
    """Predicts labels for data reveived via POST requests."""
    try:
        data = request.get_json()
        logging.debug('Received data: %s', data)

        features = [extract_features(data)]
        with open(SCALER_FILENAME, 'rb') as file:
            scaler = pickle.load(file)
        features = scaler.transform(features)

        prediction = model.predict(features)
        predicted_label = 'normal' if prediction[0] == 1 else 'anomaly'

        return jsonify(predicted_label=predicted_label)

    except (FileNotFoundError, NotFittedError) as e:
        logging.error('Error in prediction: %s', e)
        return jsonify(error=str(e)), 400


if __name__ == '__main__':
    app.run(port=8080)
