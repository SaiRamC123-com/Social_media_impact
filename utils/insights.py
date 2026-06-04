import pandas as pd

def generate_insights(df):

    insights = {}

    # Most Used Platform

    insights["Most Used Platform"] = (
        df["Platform"]
        .value_counts()
        .idxmax()
    )

    # Highest Anxiety Platform

    insights["Highest Anxiety Platform"] = (
        df.groupby("Platform")
        ["Anxiety Score"]
        .mean()
        .idxmax()
    )

    # Highest Depression Platform

    insights["Highest Depression Platform"] = (
        df.groupby("Platform")
        ["Depression Score"]
        .mean()
        .idxmax()
    )

    # Average Metrics

    insights["Average Usage"] = round(
        df["Daily Usage Hours"].mean(),
        2
    )

    insights["Average Anxiety"] = round(
        df["Anxiety Score"].mean(),
        2
    )

    insights["Average Depression"] = round(
        df["Depression Score"].mean(),
        2
    )

    insights["Average Sleep"] = round(
        df["Sleep Hours"].mean(),
        2
    )

    # High Usage Users

    insights["High Usage Users"] = len(
        df[df["Daily Usage Hours"] > 5]
    )

    # Low Sleep Users

    insights["Low Sleep Users"] = len(
        df[df["Sleep Hours"] < 6]
    )

    return insights
