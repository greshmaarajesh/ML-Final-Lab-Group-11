# G11 MetroTransit Fleet

## Forecasting Hourly Bike-Sharing Demand for Fleet Rebalancing

### Project Overview

**G11 MetroTransit Fleet** is a machine learning project focused on forecasting hourly bike-sharing demand to support efficient fleet management and rebalancing decisions.

The project uses the **UCI Bike Sharing Dataset** to analyze historical bike-sharing demand patterns, perform exploratory data analysis, develop a forecasting model, and use the predictions to support operational decision-making.

The project follows a structured workflow covering:

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Demand forecasting
* Analytics engineering and decision metrics
* Fleet rebalancing logic
* Machine learning pipeline
* Interactive dashboard
* Project documentation and presentation

---

## Project Objectives

The main objectives of this project are:

1. Analyze historical bike-sharing demand patterns.
2. Identify important factors affecting hourly bike demand.
3. Forecast future hourly bike-sharing demand.
4. Evaluate forecasting performance using suitable metrics.
5. Identify peak-demand periods and potential demand anomalies.
6. Support fleet rebalancing decisions using predicted demand.
7. Present the analysis and results through a dashboard.

---

## Dataset

The project uses the **UCI Bike Sharing Dataset**.

The dataset contains information related to bike-sharing demand, including:

* Date and time
* Season
* Year
* Month
* Hour
* Holiday
* Working day
* Weather situation
* Temperature
* Feeling temperature
* Humidity
* Windspeed
* Bike rental counts

The cleaned dataset is used for analysis and forecasting.

---

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
```

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
