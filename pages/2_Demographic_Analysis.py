import streamlit as st

from utils.data_loader import load_data
from utils.charts import age_distribution

df = load_data()

st.title("👥 Demographic Analysis")

st.plotly_chart(
    age_distribution(df),
    use_container_width=True
)
