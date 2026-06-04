import streamlit as st

from utils.data_loader import load_data
from utils.metrics import *

df = load_data()

st.title("📊 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Participants",
    total_participants(df)
)

col2.metric(
    "Avg Usage",
    avg_usage(df)
)

col3.metric(
    "Avg Anxiety",
    avg_anxiety(df)
)

col4.metric(
    "Avg Depression",
    avg_depression(df)
)
