
import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🎂 Age Group Analysis")

bins = [0,18,25,35,50,100]

labels = [
    "13-18",
    "19-25",
    "26-35",
    "36-50",
    "50+"
]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

st.subheader("Age Group Distribution")

fig = px.histogram(
    df,
    x="Age Group",
    color="Age Group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Average Anxiety by Age Group")

anxiety = (
    df.groupby("Age Group")
    ["Anxiety Score"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    anxiety,
    x="Age Group",
    y="Anxiety Score",
    color="Age Group"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader("Average Depression by Age Group")

depression = (
    df.groupby("Age Group")
    ["Depression Score"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    depression,
    x="Age Group",
    y="Depression Score",
    color="Age Group"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.subheader("Average Usage Hours by Age Group")

usage = (
    df.groupby("Age Group")
    ["Daily Usage Hours"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    usage,
    x="Age Group",
    y="Daily Usage Hours",
    color="Age Group"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)
