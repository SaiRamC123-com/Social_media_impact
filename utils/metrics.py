def total_participants(df):

    return len(df)

def avg_usage(df):

    return round(
        df["Daily Usage Hours"].mean(),
        2
    )

def avg_anxiety(df):

    return round(
        df["Anxiety Score"].mean(),
        2
    )

def avg_depression(df):

    return round(
        df["Depression Score"].mean(),
        2
    )
