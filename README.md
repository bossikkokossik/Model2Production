# Anomaly Detection in IoT: A Production-Ready Application

This repository houses a machine learning application designed for anomaly detection within IoT devices. By leveraging a dataset openly available for training, the application simulates IoT sensor output and presents prediction results through a user-friendly web-based GUI.

## 🚀 Overview

The application identifies anomalies in IoT systems and offers a streamlined experience for users through its intuitive browser-accessible interface. It serves as a tool for those looking to deploy machine learning models efficiently in the realm of IoT.

## 📋 Preliminary Information

To fully harness the capabilities of this application, certain preparatory steps are recommended.

### Prerequisites:

- A suitable dataset for model training is necessary. The [AnoML-IoT dataset on Kaggle](https://www.kaggle.com/datasets/hkayan/anomliot) is suggested as a starting point. If a different dataset is employed, column name adjustments may be required for compatibility.

### 🛠 Installation & Operation Guide

Follow this simple step-by-step installation and operation guide:

1. **Clone the Repository**:
   Retrieve the code base:
   ```sh
   git clone git@github.com:yourusername/Model2Production.git
   ```

2. **Project Directory Navigation**:
   ```sh
   cd Model2Production
   ```

3. **Dataset Integration**:
   Position the dataset file (`dataset.csv`) in the project directory.

4. **Python Environment Setup**:
   A Python environment should be created (ensure Python is installed):
   ```sh
   python -m venv .venv
   ```

5. **Environment Activation**:
   - **For Linux/MacOS**:
     ```sh
     source .venv/bin/activate
     ```
   - **For Windows**:
     ```sh
     .venv\Scripts\activate
     ```

6. **Installing Dependencies**:
   Execute the following to install necessary dependencies:
   ```sh
   python -m pip install --upgrade pip setuptools
   pip install -r requirements.txt
   ```

7. **Conducting Model Training**:
   Start the training process with the provided dataset:
   ```sh
   python train.py
   ```

8. **Prediction Server Initiation**:
   Begin the server for predictions:
   ```sh
   python server.py
   ```

9. **User Interface Activation**:
   In a new terminal window, reactivate the environment and run the UI application:
   ```sh
   python main.py
   ```

10. **Accessing the User Interface**:
    Open a web browser and navigate to:
    ```plaintext
    localhost:5000
    ```

11. **Operational Use for Anomaly Detection**:
    To test sensor data, select and submit for real-time anomaly evaluation.

12. **Terminating the Process**:
    To halt the inspection, use the `STOP` button.

13. **Conclusion of Use**:
    To finish, close the browser window and terminate the terminal sessions.

> Note: For Unix systems, the `python3` command should replace `python` in the instructions above.

---

All interested parties are welcome to star or fork this repository. Contributions to further refine and advance this anomaly detection application are appreciated. This initiative aims to enhance the security measures within IoT infrastructures. 🌟
