import pandas as pd

def generate_excel(df):

    path = (
        "reports/generated_reports/"
        "mental_health_report.xlsx"
    )

    with pd.ExcelWriter(path) as writer:

        df.to_excel(
            writer,
            sheet_name="Dataset",
            index=False
        )

        summary = pd.DataFrame({

            "Metric":[
                "Participants",
                "Avg Usage",
                "Avg Anxiety",
                "Avg Depression"
            ],

            "Value":[
                len(df),
                df["Daily Usage Hours"].mean(),
                df["Anxiety Score"].mean(),
                df["Depression Score"].mean()
            ]

        })

        summary.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

    return path
