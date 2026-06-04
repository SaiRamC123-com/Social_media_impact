from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(df):

    X = df[
        [
            "Daily Usage Hours",
            "Sleep Hours",
            "Age"
        ]
    ]

    y = df["Risk"]

    model = RandomForestClassifier()

    model.fit(X,y)

    return model
