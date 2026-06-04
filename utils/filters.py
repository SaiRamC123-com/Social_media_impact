import streamlit as st

def create_filters(df):

    gender = st.sidebar.multiselect(
        "Gender",
        df["gender"].unique(),
        default=df["gender"].unique()
    )

    platform = st.sidebar.multiselect(
        "Platform",
        df["platform_usage"].unique(),
        default=df["platform_usage"].unique()
    )

    filtered_df = df[
        (df["gender"].isin(gender))
        &
        (df["platform_usage"].isin(platform))
    ]

    return filtered_df
