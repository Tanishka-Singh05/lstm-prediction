# 🌾 Grain Spoilage Prediction Using IoT Data and LSTM with Metaheuristic Optimization

This project focuses on predicting grain spoilage in storage environments using sensor-collected IoT data. A Long Short-Term Memory (LSTM) neural network is employed to model the temporal dynamics of spoilage, and metaheuristic optimization techniques are used to fine-tune the model's hyperparameters for better accuracy and efficiency.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Tech Stack](#tech-stack)
- [Data Description](#data-description)
- [Model Architecture](#model-architecture)
- [Optimization Techniques](#optimization-techniques)
- [Results](#results)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [License](#license)

---

## 📖 Overview

Grain spoilage in storage silos causes major economic losses and food waste. By leveraging time-series sensor data (e.g., temperature, humidity, CO₂), this project predicts the onset of spoilage using LSTM neural networks. The accuracy of predictions is improved using metaheuristic algorithms (e.g., Genetic Algorithm, PSO, etc.) for hyperparameter tuning.

---

## 🎯 Objectives

- Collect and process multivariate IoT sensor data.
- Train an LSTM-based deep learning model to predict spoilage patterns.
- Apply metaheuristic algorithms to optimize hyperparameters such as learning rate, batch size, and number of LSTM layers/units.
- Evaluate model performance using RMSE, MAE, and R².
- Provide early warnings for spoilage prevention.

---

## 🧰 Tech Stack

- **Language**: Python 3.x
- **Libraries**:
    - TensorFlow / Keras
    - Scikit-learn
    - Pandas, NumPy, Matplotlib
    - Metaheuristic algorithms via `optuna`, `pyswarms`, or custom implementations
- **Notebook**: Jupyter Notebook (.ipynb)
- **Data Source**: Simulated or real-time IoT grain silo data

---

## 📊 Data Description

The dataset contains time-series sensor readings collected from grain storage environments:

| Feature        | Description                     |
|----------------|---------------------------------|
| `Temperature`  | Grain bed temperature (°C)      |
| `Humidity`     | Relative humidity (%)           |
| `CO2`          | Carbon dioxide levels (ppm)     |
| `O2`           | Oxygen levels (ppm)             |
| `Moisture`     | Moisture content (%)            |
| `SpoilageLabel`| Binary/Continuous spoilage tag  |

---

## 🧠 Model Architecture

- LSTM with stacked layers for sequential modeling
- Dropout regularization
- Dense output layer (sigmoid or linear based on problem type)
- Optimizer: Adam (with optimized learning rate)
- Loss Function: MSE / Binary Crossentropy

---

## 🧬 Optimization Techniques

Metaheuristic algorithms used for hyperparameter tuning:

- **Genetic Algorithm (GA)**
- **Particle Swarm Optimization (PSO)**
- **Bayesian Optimization**
- **Grid/Random Search (for baseline comparison)**

Tuned parameters include:
- Learning rate
- Number of LSTM units
- Number of layers
- Batch size
- Dropout rate
- Epochs

---

## 📈 Results

| Metric     | Value |
|------------|-------|
| RMSE       | XX.XX |
| MAE        | XX.XX |
| R² Score   | 0.XX  |
| Accuracy   | XX%   |

> Metaheuristically optimized models outperformed manually-tuned baselines.

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/grain-spoilage-lstm.git
cd grain-spoilage-lstm
pip install -r requirements.txt
```

## 🚀 Usage

```bash
jupyter notebook data.ipynb
```

Make sure your dataset (data.csv or similar) is placed in the project directory.

---

## 🔭 Future Work

Integration with real-time IoT devices

Deploy model as an API or edge-device-compatible tool

Add explainability via SHAP/LIME

Extend to multi-location spoilage prediction
