````markdown
# 🎮 FPS Prediction for Gaming Hardware

Welcome to the **FPS Prediction System**, a personal machine learning project focused on predicting **Frames Per Second (FPS)** for various gaming hardware and game settings. This project enables users to estimate gaming performance based on system specifications and game configurations, helping make smarter hardware and gaming decisions.

---

## 🧩 Problem Statement

**Goal:**  
Predict the FPS for a given combination of CPU, GPU, and game settings using historical benchmark data.  
**Use Case:**  
Empower gamers and hardware enthusiasts to estimate expected performance before making purchases or changing settings.

---

## 🗂️ Project Structure

```
SIH_PROJECT/
│
├── data/
│   └── raw/                  # Original datasets (Train.csv, Test.csv, etc.)
│
├── notebooks/
│   └── aiml-hackathon (3).ipynb   # Main project notebook (all logic here)
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── submission.py
│   ├── split.py
│   ├── utils.py
│   └── (other helper modules as needed)
│
├── requirements.txt
├── README.md
<<<<<<< HEAD
└── requirements.txt             # All Python dependencies
````

---

## 📌 Features

* 📉 **ARIMA Model:** Classical time-series forecasting on crop price trends.
* 🧠 **LSTM Model:** Deep learning approach for better long-term dependency capture.
* 🧹 **Preprocessing Pipeline:** Normalization, time-indexing, and missing data handling.
* 📊 **Visual Reporting:** Forecast and evaluation plots.
* 📦 **Modular Codebase:** Separated scripts for easy testing and reusability.

---

## 🖼️ Sample Visualizations

You can find screenshots and output plots inside the `reports/figures/` folder. These illustrate trends, predictions vs actual values, model evaluation metrics, etc.

---

## 📂 Dataset

We used the **Kalimati Tarkari Dataset** (publicly available), which contains:

* Historical prices of vegetables
* Market-level transaction volume
* Timestamped entries from Kalimati market

Path:
`data/raw/kalimati_tarkari_dataset.csv`

---

## 📑 Presentation

The `presentation/` folder contains the final PDF/PPT submission made for **SIH 2024**, including:

* Problem Statement
* Proposed Solution
* Architecture Diagrams
* Model Performance & Results
* Business Impact

---

## ✅ Future Scope

* Integrate with real-time APIs for live price predictions
* Deploy as a web dashboard using **Streamlit** or **FastAPI**
* Add more crops and markets across India
* Use Reinforcement Learning for decision making

---

## 👨‍💻 Authors & Team

**Xebec's Crew – SIH 2024**
Team Members:

* Anik Panja *(Lead Developer & ML Engineer)*
* \[Add others if applicable]
=======
└── LICENSE
```

## 🛠️ Workflow Overview

- **Data Loading & Exploration:**  
  Loads training and test data, explores missing values and feature correlations.

- **Data Preprocessing:**  
  Drops columns with excessive missing values, imputes missing data, identifies numeric and categorical columns.

- **Feature Engineering & Encoding:**  
  Explores encoding techniques for categorical variables (target, frequency, label encoding).  
  CatBoost is used for its native categorical support.

- **Model Training & Evaluation:**  
  - **CatBoostRegressor** is the primary model.
  - XGBoost and LightGBM are also explored.
  - Models are evaluated using RMSE and MSE.

- **Prediction & Submission:**  
  Retrains the best model on the full dataset, predicts FPS for the test set, and generates a submission CSV.

---

## 📊 Example Results

- **CatBoost** achieves the best results without explicit encoding or scaling.
- **XGBoost** and **LightGBM** provide competitive baselines.
- Test MSE (approximate):
  - XGBoost: ~2487
  - LightGBM: ~2462
>>>>>>> 5adccb0af524c98154c26578eaa90fd3ef0acdc4

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For questions or collaboration:
- 📧 [anikpanja362@gmail.com](mailto:anikpanja362@gmail.com)

---

> *Predicting gaming performance, empowering smarter hardware choices.*
````

