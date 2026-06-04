import plotly.express as px

def age_distribution(df):

    return px.histogram(
        df,
        x="Age"
    )

def anxiety_chart(df):

    return px.bar(
        df.groupby("Platform")
        ["Anxiety Score"]
        .mean()
        .reset_index(),
        x="Platform",
        y="Anxiety Score"
    )

def depression_chart(df):

    return px.bar(
        df.groupby("Platform")
        ["Depression Score"]
        .mean()
        .reset_index(),
        x="Platform",
        y="Depression Score"
    )
