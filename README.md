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

The project uses the **UCI Bike Sharing Dataset**.

The dataset contains information related to bike-sharing demand, including:

- Date and time
- Season
- Year
- Month
- Hour
- Holiday
- Working day
- Weather situation
- Temperature
- Feeling temperature
- Humidity
- Windspeed
- Bike rental counts

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

The primary forecasting metric is:

**RMSE — Root Mean Squared Error**

RMSE measures the magnitude of prediction errors and gives greater weight to larger errors.

### Additional Evaluation Metrics

The project also evaluates:

- **MAPE — Mean Absolute Percentage Error**
- **Hourly Peak Error**

These metrics provide additional information about overall forecasting accuracy and performance during high-demand periods.

### Baseline Performance

The baseline model is used as the reference point for evaluating the forecasting models developed in the project.

**Baseline Model:** Baseline forecasting model

**Primary Metric:** RMSE

**Baseline RMSE:** To be updated from the final model evaluation results

**Baseline MAPE:** To be updated from the final model evaluation results

**Baseline Hourly Peak Error:** To be updated from the final model evaluation results

---

## 7. Methodology

The project follows a time-series-aware machine learning workflow.

```text
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

## Repository Structure

```text

G11_MetroTransit_Fleet/
│
├── Data/
│   ├── Original_Dataset.csv
│   └── Cleaned_Dataset.csv
│
├── Data_Analysis/
│   └── EDA.ipynb
│
├── Forecasting/
│   └── Forecasting_Model.ipynb
│
├── Analytics_Engineering/
│   ├── Metrics_Analysis.ipynb
│   ├── Rebalancing_Logic.py
│   └── Decision_Metrics.csv
│
├── ML_Pipeline/
│   ├── predict.py
│   ├── model.pkl
│   └── requirements.txt
│
├── Dashboard/
│   └── MetroTransit_Fleet.pbix
│
├── Report/
│   └── Project_Report.docx
│
├── Presentation/
│   └── MetroTransit_Fleet_Presentation.pptx
│
└── README.md


---

## Forecasting Methodology

The project follows a **time-series-aware validation approach** to maintain the chronological order of the data.

Future observations should not be used to train models for predicting earlier observations. This helps prevent **data leakage** and provides a more realistic evaluation of forecasting performance.

The main evaluation metrics include:

### RMSE

**Root Mean Squared Error (RMSE)** measures the average magnitude of prediction errors while giving greater weight to larger errors.

### MAPE

**Mean Absolute Percentage Error (MAPE)** measures prediction error as a percentage of actual demand.

### Hourly Peak Error

This metric focuses specifically on forecasting performance during important high-demand periods.

---

## Expected Outcome

The final project aims to provide a complete workflow from historical bike-sharing data to demand forecasting and fleet rebalancing support.

The expected workflow is:

```text
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

---

## Team

**Group 11 – MetroTransit Fleet**

The project is developed collaboratively by the members of Group 11, with different members contributing to data analysis, forecasting, analytics engineering, machine learning pipeline development, dashboard creation, documentation, and presentation.
