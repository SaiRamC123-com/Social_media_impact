import pandas as pd

def get_summary(df):

    summary = {

        "Total Participants": len(df),

        "Average Usage Hours":
        round(df["Daily Usage Hours"].mean(),2),

        "Average Anxiety":
        round(df["Anxiety Score"].mean(),2),

        "Average Depression":
        round(df["Depression Score"].mean(),2),

        "Average Sleep":
        round(df["Sleep Hours"].mean(),2)

    }

    return summary
