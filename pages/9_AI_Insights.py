import streamlit as st

from utils.data_loader import load_data

df = load_data()

st.title("🧠 AI Insights")

st.subheader("Key Findings")

most_used_platform = (
    df["Platform"]
    .value_counts()
    .idxmax()
)

highest_anxiety_platform = (
    df.groupby("Platform")
    ["Anxiety Score"]
    .mean()
    .idxmax()
)

highest_depression_platform = (
    df.groupby("Platform")
    ["Depression Score"]
    .mean()
    .idxmax()
)

high_usage = len(
    df[
        df["Daily Usage Hours"] > 5
    ]
)

st.success(
    f"📱 Most Used Platform: {most_used_platform}"
)

st.info(
    f"😟 Highest Anxiety Platform: {highest_anxiety_platform}"
)

st.warning(
    f"😔 Highest Depression Platform: {highest_depression_platform}"
)

st.error(
    f"⚠️ Users Spending More Than 5 Hours: {high_usage}"
)

st.divider()

st.subheader("AI Recommendations")

st.markdown("""
### Recommendations

✅ Limit social media usage to less than 4 hours/day

✅ Maintain 7–8 hours of sleep

✅ Schedule regular digital detox sessions

✅ Track anxiety and depression symptoms

✅ Encourage outdoor activities and exercise

✅ Reduce late-night social media usage
""")

st.divider()

st.subheader("Mental Health Risk Summary")

avg_usage = round(
    df["Daily Usage Hours"].mean(),
    2
)

avg_anxiety = round(
    df["Anxiety Score"].mean(),
    2
)

avg_depression = round(
    df["Depression Score"].mean(),
    2
)

st.metric(
    "Average Usage Hours",
    avg_usage
)

st.metric(
    "Average Anxiety Score",
    avg_anxiety
)

st.metric(
    "Average Depression Score",
    avg_depression
)

st.subheader("Dataset Preview")

st.dataframe(df.head(20))
