import streamlit as st

from utils.data_loader import load_data
from utils.charts import anxiety_chart

df = load_data()

st.title("🧠 Mental Health Analysis")

st.plotly_chart(
    anxiety_chart(df),
    use_container_width=True
)
