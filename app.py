import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="NASA Predictive Maintenance",
    page_icon="✈️",
    layout="wide"
)

# Title
st.title("NASA C-MAPSS Predictive Maintenance Dashboard")
st.write("Aircraft Engine Remaining Useful Life (RUL) Prediction")
st.markdown("---")

# Engine Health Summary
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

# Health Status
st.header("Engine Health Status")

health_data = pd.DataFrame({
    "Health Status": ["Normal", "Warning", "Critical"],
    "Number of Engines": [2854, 672, 544]
})

st.bar_chart(
    health_data.set_index("Health Status")
)

st.markdown("---")

# Model Performance
st.header("Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("MAE", "10.81 cycles")

with col2:
    st.metric("RMSE", "15.93 cycles")

with col3:
    st.metric("R² Score", "0.854")

st.markdown("---")

# RUL Prediction
st.header("RUL Prediction")

cycle = st.number_input(
    "Enter Current Cycle",
    min_value=1,
    value=1,
    step=1
)

if st.button("Predict RUL"):
    st.success(f"Current Cycle: {cycle}")
    st.info(
        "The Random Forest based RUL prediction system is ready."
    )

st.markdown("---")

st.caption(
    "NASA C-MAPSS Predictive Maintenance | "
    "Machine Learning using Random Forest"
)
