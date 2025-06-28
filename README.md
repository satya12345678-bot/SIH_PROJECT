
#  Crop Price Prediction System + Web Interface to publish results - SIH 2024

Welcome to the **Crop Price Prediction System + Web interface**, a data science, machine learning and Web development project developed for the **Smart India Hackathon (SIH) 2024** by team **Xebec's Crew**.

This project focuses on predicting market prices of vegetables using historical data and time-series modeling techniques than publishing them on the website, with the ultimate goal of helping farmers and government to make informed decisions on crop sales and logistics.

---

## Problem Statement

**Domain:** Agriculture & Market Linkage  
**Challenge:** Predict future vegetable market prices using past data to support price transparency, optimize supply-chain decisions, and provide an interface for the input and results.

---

## Project Structure

```bash
SIH_PROJECT/
│
├── data/
│   ├── raw/                       # Original input files (CSV, PDFs)
│   │   └── kalimati_tarkari_dataset.csv
│   │   └── SIH2024_1647_Xebec's_Crew.pdf
│
├── reports/
│   ├── figures/                  # Visualizations and model performance plots
│   │   └── Screenshot_*.png
│
├── src/                          # Source code for data loading, modeling, utils
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── arima_model.py
│   ├── lstm_model.py
│   └── utils.py
│
├── presentation/                # SIH submission and PPTs
│   └── (Your final presentation slides or PDF)
│
├── LICENSE
├── README.md
└── requirements.txt             # All Python dependencies
````

---

##  How to Run the Project

### 1. Install Dependencies

Make sure you are using Python 3.8+. Then run:

```bash
pip install -r requirements.txt
```

---

### 2. Load and Preprocess the Data

```bash
python src/data_loader.py
python src/preprocessing.py
```

---

### 3. Train Models

#### ARIMA Model:

```bash
python src/arima_model.py
```

#### LSTM Model:

```bash
python src/lstm_model.py
```

---

### 📈 4. Visualize Results

All generated plots (model loss, price forecasts, trend analysis) will be saved in the:

```bash
reports/figures/
```

---

## Features

*    **ARIMA Model:** Classical time-series forecasting on crop price trends.
*    **LSTM Model:** Deep learning approach for better long-term dependency capture.
*    **Preprocessing Pipeline:** Normalization, time-indexing, and missing data handling.
*    **Visual Reporting:** Forecast and evaluation plots.
*    **Modular Codebase:** Separated scripts for easy testing and reusability.

---

## Sample Visualizations

You can find screenshots and output plots inside the `reports/figures/` folder. These illustrate trends, predictions vs actual values, model evaluation metrics, etc.

---

## Dataset

We used the **Kalimati Tarkari Dataset** (publicly available), which contains:

* Historical prices of vegetables
* Market-level transaction volume
* Timestamped entries from Kalimati market

Path:
`data/raw/kalimati_tarkari_dataset.csv`

---

## Presentation

The `presentation/` folder contains the final PDF/PPT submission made for **SIH 2024**, including:

* Problem Statement
* Proposed Solution
* Architecture Diagrams
* Model Performance & Results
* Business Impact

---

## Future Scope

* Integrate the model into the Website.
* Add more crops and markets across India
* Use Reinforcement Learning for decision making

---

## Authors & Team

**Xebec's Crew – SIH 2024**
Team Members:
* Mridul Chouhan *(Team Leader)*
* Anik Panja *(ML Engineer)*
* Arkadip Ghara *(ML Engineer)*
* Siddharth Patel *(Finance Analyst)*
* Satyabratta Biswal *(Pitch Deck creator)*

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or collaborations:
* 📧 [MridulChouhan@gmail.com](mailto:strangemridul@gmail.com)
* 📧 [anikpanja362@gmail.com](mailto:anikpanja362@example.com) 

---

