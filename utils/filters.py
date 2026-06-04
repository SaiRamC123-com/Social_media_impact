import streamlit as st

def sidebar_filters(df):

    gender = st.sidebar.multiselect(
        "Gender",
        df["Gender"].unique(),
        default=df["Gender"].unique()
    )

    platform = st.sidebar.multiselect(
        "Platform",
        df["Platform"].unique(),
        default=df["Platform"].unique()
    )

    filtered = df[
        (df["Gender"].isin(gender))
        &
        (df["Platform"].isin(platform))
    ]

    return filtered
