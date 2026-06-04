def total_students(df):

    return len(df)


def avg_age(df):

    return round(
        df["age"].mean(),
        2
    )


def avg_social_media(df):

    return round(
        df["daily_social_media_hours"].mean(),
        2
    )


def avg_sleep(df):

    return round(
        df["sleep_hours"].mean(),
        2
    )


def avg_stress(df):

    return round(
        df["stress_level"].mean(),
        2
    )


def avg_anxiety(df):

    return round(
        df["anxiety_level"].mean(),
        2
    )


def avg_addiction(df):

    return round(
        df["addiction_level"].mean(),
        2
    )


def depression_rate(df):

    return round(
        df["depression_label"].mean()*100,
        2
    )
