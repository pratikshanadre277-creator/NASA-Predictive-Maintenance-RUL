import streamlit as st

st.title("NASA Predictive Maintenance")
st.write("Aircraft Engine Remaining Useful Life (RUL) Prediction")

st.header("RUL Prediction")

cycle = st.number_input("Enter Current Cycle", min_value=1, value=1)

if st.button("Predict RUL"):
    st.success(f"Current cycle: {cycle}")
    st.info("RUL prediction system is ready.")
