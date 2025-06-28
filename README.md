````markdown
# 🥑 Fruit Price Prediction Using RNN-LSTM & ARIMA

Welcome to the **Fruit Price Prediction System**, a machine learning project focused on forecasting fruit and vegetable prices using both classical and deep learning time series models. This project leverages the Kalimati Tarkari dataset and demonstrates a full workflow from data preprocessing to ARIMA and LSTM modeling, including anomaly detection with Bollinger Bands.

---

## 🏆 Hackathon Context

This project was developed as part of the **Smart India Hackathon (SIH)**, where our team, **Xebec's Crew**, participated to address real-world agricultural challenges using data science and AI.

---

## 🧩 Problem Statement

**Goal:**  
Predict the future average price of a selected fruit or vegetable using historical market data , and also send buffer stocks to places where needed.

**Use Case:**  
Empower farmers, traders, and policymakers to anticipate price trends, optimize sales, and make informed decisions.

---

## 🗂️ Project Structure

```
SIH_PROJECT/
│
├── data/
│   └── raw/
│       └── kalimati_tarkari_dataset.csv   # Main dataset
│
├── notebooks/
│   └── arima_lstm_model.ipynb             # Main notebook (all logic here)
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── arima.py
│   ├── lstm.py
│   ├── bollinger.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Workflow Overview

- **Data Loading & Mapping:**  
  Loads the Kalimati dataset and anonymizes commodity names using US state codes for demonstration.

- **PreProcessing:**  
  - Filters for a selected commodity (e.g., "NV")
  - Groups by date and averages prices
  - Handles missing values (forward fill)
  - Splits into train/test sets

- **Visualization:**  
  - Plots time series and missing value diagnostics

- **ARIMA Modeling:**  
  - Stationarity checks (ADF test, differencing)
  - Model fitting and forecasting
  - Evaluation (MAE, relative error)
  - Plots actual vs. forecasted prices

- **LSTM Modeling:**  
  - Windowed dataset creation for sequence learning
  - Deep learning model with Conv1D + Bidirectional LSTM layers
  - Learning rate scheduling and training
  - Evaluation and forecast visualization

- **Bollinger Bands & Anomaly Detection:**  
  - Calculates moving average and bands
  - Plots predictions with bands
  - Identifies dates where predictions exceed normal volatility

---

## 📊 Example Results

- **ARIMA** and **LSTM** models both provide price forecasts.
- **Bollinger Bands** highlight periods of unusual price movement.
- Evaluation metrics (e.g., MAE) are printed for both models.

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
* Mridul Chauhan (Team Leader)
* Anik Panja *(Lead ML Engineer)*
* Arkadip Ghara
* Satyabrata Biswal
* Siddharth Patel

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For questions or collaboration:
- 📧 [anikpanja362@gmail.com](mailto:anikpanja362@gmail.com)

---

> *Predicting agricultural prices, empowering smarter market decisions.*
````

