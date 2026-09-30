# G11 MetroTransit Fleet

## Forecasting Hourly Bike-Sharing Demand for Fleet Rebalancing

---

## 1. Team & Member Roster

### Group 11

**G11 MetroTransit Fleet**

### Team Members

| Functional Role | Team Member | Core Responsibilities |
|---|---|---|
| **Data Engineer (DE)** | Varshitha K R | Data acquisition, validation, cleaning, preprocessing, data quality, and leakage prevention |
| **Data Analyst (DA)** | Greshmaa Rajesh | Visual and statistical EDA, distribution and skewness analysis, correlation analysis, feature interactions, and actionable insights |
| **Data Scientist (DS)** | A Merlin Levia | Model development, baseline comparison, algorithm selection, hyperparameter tuning, and cross-validation |
| **Analytics Engineer (AE)** | Shiny Matilda K | Connecting cleaned data, model predictions, and business KPIs; developing decision metrics and rebalancing logic |
| **ML Engineer (MLE)** | V Mounisha | Reproducible inference pipeline, prediction script, model management, dependencies, and pipeline testing |
| **BI / Power BI Developer (BI)** | Angel Precilla A | Interactive Power BI dashboard, KPI visualization, operational insights, and dashboard usability |

---

## 2. Client Persona

### Client

**MetroTransit Fleet Management**

### Client Persona

The client is a **bike-sharing fleet management team** responsible for ensuring that bicycles are available when and where demand is high.

The fleet management team needs to make operational decisions regarding:

- When demand is expected to increase
- When demand is expected to decrease
- When bike shortages may occur
- When bikes should be redistributed
- How fleet resources can be allocated efficiently

---

## 3. Problem Statement

Bike-sharing demand varies significantly depending on factors such as **hour, season, weather, temperature, humidity, working day, and holidays**.

Without reliable demand forecasts, fleet operators may experience:

- Bike shortages during high-demand periods
- Excess bikes during low-demand periods
- Inefficient fleet redistribution
- Poor utilization of available bicycles

### Project Problem

> **Develop a machine learning-based forecasting solution to predict hourly bike-sharing demand and use the predictions to support fleet rebalancing decisions.**

The project uses historical bike-sharing data to identify demand patterns, forecast future hourly demand, evaluate prediction performance, and generate operational insights for fleet management.

---

## 4. Dataset

The project uses the **UCI Bike Sharing Dataset (hourly)**, containing 17,379 hourly records from 2011–2012.

Key fields include:

- Date and time
- Season, Year, Month, Hour
- Holiday, Working day
- Weather situation, Temperature, Feeling temperature, Humidity, Windspeed
- Bike rental counts (casual, registered, total)

The target variable for forecasting is **hourly bike rental demand (`cnt`)**.

---

## 5. Project Objectives

1. Analyze historical bike-sharing demand patterns.
2. Identify important factors affecting hourly bike demand.
3. Forecast future hourly bike-sharing demand.
4. Evaluate forecasting performance using suitable metrics.
5. Identify peak-demand periods and potential demand anomalies.
6. Support fleet rebalancing decisions using predicted demand.
7. Present the analysis and results through an interactive dashboard.

---

## 6. Primary Target Metric & Baseline Performance

### Primary Target Metric

**RMSE — Root Mean Squared Error**

RMSE measures the magnitude of prediction errors and gives greater weight to larger errors, which matters here since large misses during peak hours are the most operationally costly.

### Additional Evaluation Metrics

- **R² — Coefficient of Determination**
- **MAPE — Mean Absolute Percentage Error**
- **Peak-Hour Error** (RMSE and MAPE restricted to the top 10% highest-demand hours)

### Model & Baseline Performance

**Model:** Random Forest Regressor, tuned via `GridSearchCV` with `TimeSeriesSplit` (5 folds), trained on a log-transformed target with cyclic hour/month feature engineering.

**Evaluation set:** Chronological holdout of 3,476 hours (7 Aug – 31 Dec 2012), kept time-ordered relative to training to avoid future data leakage.

| Metric | Overall | Peak-Demand Hours (top 10%) |
|---|---|---|
| RMSE | **88.76** | 181.86 |
| R² | **0.838** | — |
| MAPE | **32.85%** | 20.73% |

**Rebalancing outcome:** Testing safety margins from 0% to 40%, a **35% safety margin** gave the lowest total modelled operational cost (**$358,217.50**), saving an estimated **41.5%** ($254,114.75) compared with a 0% margin over the 147-day holdout period.

---

## 7. Methodology

The project follows a time-series-aware machine learning workflow:
```
Historical Bike-Sharing Data
↓
Data Preprocessing
↓
Exploratory Data Analysis
↓
Feature Engineering
↓
Demand Forecasting
↓
Model Evaluation
↓
Analytics Engineering
↓
Rebalancing Logic
↓
Operational Insights
↓
Power BI Dashboard
```

The project follows a **time-series-aware validation approach** to maintain the chronological order of the data. Future observations are not used to train models for predicting earlier observations, which prevents **data leakage** and gives a more realistic evaluation of forecasting performance.

---

## 8. Repository Structure
```
ML-Final-Lab-Group-11/
│
├── README.md
├── requirements.txt
│
├── cleaned_bike_sharing.csv
├── Holdout_Predictions.csv
├── Decision_Metrics.csv
│
├── data/
│ ├── processed/
│   └──cleaned_bike_sharing.csv
│ ├── raw/
│   └──hour.csv
│ 
├── notebooks/
│ └──EDA.ipynb
│ └──ML_Project .ipynb
│ └──Metrics_Analysis.ipynb
│ └──Preprocessing (1).ipynb
│ └──Rebalancing_Logic.py
│ └──_Forecasting_Model_.ipynb
│ └──_Predict.py

cleaned_bike_sharing.csv
│
├── src/
│ └── (supporting scripts, if any)
│
├── dashboard/
│ └── metrotransit fleet.pbix
│
├── report/
│ └── MetroTransit_Fleet_Project_Report.docx
│
└── presentation/
└── Client_Pitch.pptx
```
