import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/Teen_Mental_Health_Dataset.csv"
    )

    return df
