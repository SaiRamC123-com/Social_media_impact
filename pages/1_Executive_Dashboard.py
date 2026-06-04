import streamlit as st

from utils.data_loader import load_data
from utils.metrics import *
from utils.filters import create_filters

df = load_data()

df = create_filters(df)

st.title("📊 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Students",
    total_students(df)
)

col2.metric(
    "Avg Age",
    avg_age(df)
)

col3.metric(
    "Avg Social Media Hours",
    avg_social_media(df)
)

col4.metric(
    "Depression Rate %",
    depression_rate(df)
)

col1,col2,col3 = st.columns(3)

col1.metric(
    "Stress",
    avg_stress(df)
)

col2.metric(
    "Anxiety",
    avg_anxiety(df)
)

col3.metric(
    "Addiction",
    avg_addiction(df)
)
