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

