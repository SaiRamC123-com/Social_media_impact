import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("👨‍🦰👩 Gender Analysis")

st.subheader("Gender Distribution")

gender_count = (
    df["Gender"]
    .value_counts()
    .reset_index()
)

fig = px.pie(
    gender_count,
    names="Gender",
    values="count",
    title="Gender Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Average Anxiety by Gender")

anxiety_gender = (
    df.groupby("Gender")
    ["Anxiety Score"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    anxiety_gender,
    x="Gender",
    y="Anxiety Score",
    color="Gender"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader("Average Depression by Gender")

depression_gender = (
    df.groupby("Gender")
    ["Depression Score"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    depression_gender,
    x="Gender",
    y="Depression Score",
    color="Gender"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.subheader("Average Sleep Hours by Gender")

sleep_gender = (
    df.groupby("Gender")
    ["Sleep Hours"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    sleep_gender,
    x="Gender",
    y="Sleep Hours",
    color="Gender"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)
