import streamlit as st

from utils.data_loader import load_data
from utils.ml_models import train_model

df = load_data()

model = train_model(df)

st.title("🤖 Mental Health Risk Prediction")

usage = st.slider(
    "Daily Usage Hours",
    0.0,
    12.0,
    3.0
)

sleep = st.slider(
    "Sleep Hours",
    1.0,
    12.0,
    7.0
)

age = st.slider(
    "Age",
    13,
    60,
    25
)

if st.button("Predict Risk"):

    prediction = model.predict(
        [[usage,sleep,age]]
    )[0]

    st.success(
        f"Predicted Risk Level: {prediction}"
    )
