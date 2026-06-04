import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data

st.set_page_config(
    page_title="Demographic Analysis",
    page_icon="👥",
    layout="wide"
)

df = load_data()

st.title("👥 Demographic Analysis")

# -----------------------------
# Dataset Overview
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Participants",
        len(df)
    )

with col2:
    st.metric(
        "Average Age",
        round(df["age"].mean(), 2)
    )

with col3:
    st.metric(
        "Depression %",
        round(df["depression_label"].mean() * 100, 2)
    )

st.divider()

# -----------------------------
# Age Distribution
# -----------------------------

st.subheader("📊 Age Distribution")

fig_age = px.histogram(
    df,
    x="age",
    nbins=15,
    title="Age Distribution"
)

st.plotly_chart(
    fig_age,
    use_container_width=True
)

# -----------------------------
# Gender Distribution
# -----------------------------

st.subheader("👨‍🦰 Gender Distribution")

gender_df = (
    df["gender"]
    .value_counts()
    .reset_index()
)

gender_df.columns = [
    "Gender",
    "Count"
]

fig_gender = px.pie(
    gender_df,
    names="Gender",
    values="Count",
    title="Gender Distribution"
)

st.plotly_chart(
    fig_gender,
    use_container_width=True
)

# -----------------------------
# Age vs Depression
# -----------------------------

st.subheader("🧠 Age vs Depression")

fig_dep = px.box(
    df,
    x="depression_label",
    y="age",
    color="depression_label"
)

st.plotly_chart(
    fig_dep,
    use_container_width=True
)

# -----------------------------
# Gender vs Depression
# -----------------------------

st.subheader("📈 Gender vs Depression")

gender_dep = (
    df.groupby("gender")["depression_label"]
    .mean()
    .reset_index()
)

gender_dep["depression_label"] = (
    gender_dep["depression_label"] * 100
)

fig_gender_dep = px.bar(
    gender_dep,
    x="gender",
    y="depression_label",
    color="gender",
    title="Depression Percentage by Gender"
)

st.plotly_chart(
    fig_gender_dep,
    use_container_width=True
)

# -----------------------------
# Age Group Analysis
# -----------------------------

st.subheader("🎂 Age Group Analysis")

df["Age Group"] = pd.cut(
    df["age"],
    bins=[12, 15, 17, 19],
    labels=[
        "13-15",
        "16-17",
        "18-19"
    ]
)

age_group_df = (
    df.groupby("Age Group")
    .size()
    .reset_index(name="Count")
)

fig_age_group = px.bar(
    age_group_df,
    x="Age Group",
    y="Count",
    color="Age Group"
)

st.plotly_chart(
    fig_age_group,
    use_container_width=True
)

# -----------------------------
# Raw Dataset Preview
# -----------------------------

with st.expander("View Dataset"):

    st.dataframe(
        df.head(20),
        use_container_width=True
    )
