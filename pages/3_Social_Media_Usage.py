import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("📱 Social Media Usage")

fig = px.histogram(
    df,
    x="Daily Usage Hours"
)

st.plotly_chart(fig)
