import joblib
import numpy as np
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Bike Sharing Demand Prediction",
    page_icon="🚲",
    layout="centered",
)

st.title("🚲 Bike Sharing Demand Prediction")
st.write("Predict bike rental demand using time and weather conditions.")


# 2. Load Trained Model
@st.cache_resource
def load_model():
    return joblib.load("bike_demand_model.pkl")


try:
    model = load_model()
except Exception as e:
    st.error(
        f"Could not load 'bike_demand_model.pkl'. Make sure the model file is in the same folder as app.py!"
    )
    st.stop()

# 3. Form Inputs
st.subheader("Select Input Variables")

col1, col2 = st.columns(2)

with col1:
    season = st.selectbox(
        "Season",
        [1, 2, 3, 4],
        format_func=lambda x: {
            1: "1: Spring",
            2: "2: Summer",
            3: "3: Fall",
            4: "4: Winter",
        }[x],
    )
    yr = st.selectbox(
        "Year", [0, 1], format_func=lambda x: "2011" if x == 0 else "2012"
    )
    mnth = st.slider("Month", min_value=1, max_value=12, value=1)
    hr = st.slider("Hour of Day (0-23)", min_value=0, max_value=23, value=8)
    weekday = st.selectbox(
        "Day of Week",
        list(range(7)),
        format_func=lambda x: [
            "Sun",
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
        ][x],
    )
    workingday = st.selectbox(
        "Working Day?",
        [1, 0],
        format_func=lambda x: "Yes" if x == 1 else "No",
    )

with col2:
    holiday = st.selectbox(
        "Holiday?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"
    )
    weathersit = st.selectbox(
        "Weather Condition",
        [1, 2, 3, 4],
        format_func=lambda x: {
            1: "1: Clear / Few Clouds",
            2: "2: Mist / Cloudy",
            3: "3: Light Snow / Rain",
            4: "4: Heavy Rain / Snow",
        }[x],
    )
    temp = st.slider(
        "Normalized Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.25,
        step=0.01,
    )
    atemp = st.slider(
        "Normalized Feeling Temp",
        min_value=0.0,
        max_value=1.0,
        value=0.29,
        step=0.01,
    )
    hum = st.slider(
        "Normalized Humidity",
        min_value=0.0,
        max_value=1.0,
        value=0.81,
        step=0.01,
    )
    windspeed = st.slider(
        "Normalized Windspeed",
        min_value=0.0,
        max_value=1.0,
        value=0.0,
        step=0.01,
    )


# 4. Feature Engineering & Prediction Pipeline
def predict_demand(raw_input):
    df = pd.DataFrame([raw_input])

    # Add cyclic representations for hour and month
    df["sin_hr"] = np.sin(2 * np.pi * df["hr"] / 24.0)
    df["cos_hr"] = np.cos(2 * np.pi * df["hr"] / 24.0)
    df["sin_mnth"] = np.sin(2 * np.pi * df["mnth"] / 12.0)
    df["cos_mnth"] = np.cos(2 * np.pi * df["mnth"] / 12.0)

    # Order columns as required by model
    model_columns = [
        "season",
        "yr",
        "mnth",
        "hr",
        "holiday",
        "weekday",
        "workingday",
        "weathersit",
        "temp",
        "atemp",
        "hum",
        "windspeed",
        "sin_hr",
        "cos_hr",
        "sin_mnth",
        "cos_mnth",
    ]
    df = df[model_columns]

    # Predict log output & convert back to original scale
    log_pred = model.predict(df)[0]
    real_pred = np.expm1(log_pred)
    return max(0.0, real_pred)


# 5. Predict Button
st.divider()
if st.button("Predict Bike Demand", type="primary", use_container_width=True):
    raw_input = {
        "season": season,
        "yr": yr,
        "mnth": mnth,
        "hr": hr,
        "holiday": holiday,
        "weekday": weekday,
        "workingday": workingday,
        "weathersit": weathersit,
        "temp": temp,
        "atemp": atemp,
        "hum": hum,
        "windspeed": windspeed,
    }

    result = predict_demand(raw_input)
    st.success(
        f"### Predicted Demand: **{int(round(result))} bikes** for this hour"
    )
