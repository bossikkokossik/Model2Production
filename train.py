"""
The module responsible for training the model that shall be used for anomaly 
detection. After training the model is saved, so that it can be reused by
other modules. The same holds for the scaler in order to ensure proper data
processing.
"""

from pathlib import Path
import pickle

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, silhouette_score)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def train(dataset_filename):
    """
    Carries out the process for training a model to be used in the product:
        - loads data from the dataset
        - processes data so that they can be properly read by the algorithm
        - performs the training
        - calculates performance metric
        - saves both scaler and model for external usage
        - shows prediction visualisation for the test data
    """
    df = pd.read_csv(dataset_filename)
    X = df[['Temperature', 'Humidity', 'Loudness']].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    with open('scaler.pkl', 'wb') as file:
        pickle.dump(scaler, file)

    clf = IsolationForest(contamination=0.05, n_estimators=200,
                          max_features=0.8, random_state=42)
    model = clf.fit(X_scaled)
    df['Label'] = clf.predict(X_scaled)
    df['Label'] = df['Label'].replace({1: 'normal', -1: 'anomaly'})

    _, X_test, _, y_test = train_test_split(
        X_scaled, df['Label'], test_size=0.2, random_state=42)

    y_pred = clf.predict(X_test)
    y_pred_label = ['normal' if label == 1 else 'anomaly' for label in y_pred]

    print(f'Accuracy Score: {accuracy_score(y_test, y_pred_label)}')
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred_label))
    print('Classification Report:\n',
          classification_report(y_test, y_pred_label))
    print(f'Silhouette Score: {silhouette_score(X_test, y_pred)}')

    model_path = Path('.')
    model_filename = Path('trained_model.pkl')
    with open(model_path / model_filename, 'wb') as file:
        pickle.dump(model, file)

    color_dict = {'normal': 'green', 'anomaly': 'red'}
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Humidity')
    ax.set_zlabel('Loudness')
    ax.scatter(X_test[:, 0], X_test[:, 1], X_test[:, 2], c=[
               color_dict[label] for label in y_pred_label])
    plt.show()


if __name__ == '__main__':
    train('dataset_final.csv')
