# ML_Group-11
# MetroTransit Fleet – Smart Mobility

## Project Overview

G11 MetroTransit Fleet – Smart Mobility is a data analytics and machine learning project that forecasts hourly bike-sharing demand to support fleet rebalancing decisions.

The project uses the UCI Bike Sharing Dataset to analyze historical bike demand based on factors such as hour, season, weather, temperature, humidity, working days, and holidays.

## Objectives

- Analyze historical bike-sharing demand.
- Identify hourly, seasonal, and weather-related demand patterns.
- Perform exploratory data analysis (EDA).
- Build a model to forecast hourly bike demand.
- Evaluate predictions using RMSE, MAPE, and Hourly Peak Error.
- Maintain time-series ordering and prevent future-data leakage.
- Develop fleet-rebalancing decision logic.
- Visualize results using Power BI.

## Project Workflow

Dataset

↓

Data Engineering

↓

Data Analysis / EDA

↓

Feature Engineering & Forecasting

↓

Model Evaluation

↓

Fleet Rebalancing Logic

↓

ML Prediction Pipeline

↓

Power BI Dashboard

↓

Final Presentation


## Dataset

The project uses the UCI Bike Sharing Dataset.

### Important Variables

| Variable | Description |
|---|---|
| `dteday` | Date |
| `hr` | Hour |
| `season` | Season |
| `holiday` | Holiday indicator |
| `weekday` | Day of the week |
| `workingday` | Working/non-working day |
| `weathersit` | Weather condition |
| `temp` | Temperature |
| `atemp` | Feeling temperature |
| `hum` | Humidity |
| `windspeed` | Wind speed |
| `casual` | Casual users |
| `registered` | Registered users |
| `cnt` | Total bike demand |

The primary prediction target is `cnt`, representing total hourly bike demand.

## Model Evaluation

The forecasting model is evaluated using:

- **RMSE (Root Mean Squared Error)** – measures prediction error.
- **MAPE (Mean Absolute Percentage Error)** – measures percentage error.
- **Hourly Peak Error** – evaluates prediction performance during peak-demand hours.

## Time-Series Validation

The project follows strict temporal ordering during model validation.

- Past data is used for training.
- Later data is used for validation/testing.
- Future information is not used to predict earlier periods.
- Random splitting is avoided where it could cause data leakage.

## Fleet Rebalancing

Predicted demand is compared with available fleet capacity to identify potential:

- Bike shortages
- Bike surpluses
- Normal-demand periods

These results are used to support fleet-rebalancing decisions.

## Project Structure
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
│   ├── preprocessing.py
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
