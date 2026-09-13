import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(
    page_title="NASA Predictive Maintenance",
    page_icon="✈️",
    layout="wide"
)

# Load trained model
model = joblib.load("model.pkl")

st.title("NASA C-MAPSS Predictive Maintenance Dashboard")
st.write("Aircraft Engine Remaining Useful Life (RUL) Prediction")
st.markdown("---")

# Dashboard summary
st.header("Engine Health Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Predictions", "4,070")
    st.metric("Average Predicted RUL", "87.52 cycles")

with col2:
    st.metric("Minimum Predicted RUL", "1.62 cycles")
    st.metric("Normal", "2,854")

with col3:
    st.metric("Warning", "672")
    st.metric("Critical", "544")

st.markdown("---")

# Health status
st.header("Engine Health Status")

health_data = pd.DataFrame({
    "Health Status": ["Normal", "Warning", "Critical"],
    "Number of Engines": [2854, 672, 544]
})

st.bar_chart(
    health_data.set_index("Health Status")
)

st.markdown("---")

# Model performance
st.header("Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("MAE", "10.81 cycles")

with col2:
    st.metric("RMSE", "15.93 cycles")

with col3:
    st.metric("R² Score", "0.854")

st.markdown("---")

# Prediction section
st.header("RUL Prediction")

st.write("Enter engine operating parameters:")

cycle = st.number_input(
    "Current Cycle",
    min_value=1.0,
    value=1.0
)

setting_1 = st.number_input("Setting 1", value=0.0)
setting_2 = st.number_input("Setting 2", value=0.0)
setting_3 = st.number_input("Setting 3", value=0.0)

st.subheader("Sensor Values")

sensor_values = []

for i in [2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 20, 21]:
    value = st.number_input(
        f"Sensor {i}",
        value=0.0
    )
    sensor_values.append(value)

if st.button("Predict RUL"):

    input_data = pd.DataFrame([[
        cycle,
        setting_1,
        setting_2,
        setting_3,
        *sensor_values
    ]])

    prediction = model.predict(input_data)[0]

    prediction = max(0, prediction)

    st.success(
        f"Predicted Remaining Useful Life: {prediction:.2f} cycles"
    )

    if prediction <= 30:
        st.error("Critical: Engine requires immediate attention.")
    elif prediction <= 60:
        st.warning("Warning: Engine requires monitoring.")
    else:
        st.info("Normal: Engine health is satisfactory.")

st.markdown("---")

st.caption(
    "NASA C-MAPSS Predictive Maintenance | "
    "Machine Learning using Random Forest"
)
