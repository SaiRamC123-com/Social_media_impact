import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("📲 Platform Comparison")

fig = px.box(
    df,
    x="Platform",
    y="Anxiety Score"
)

st.plotly_chart(fig)
