from reports.report_utils import (
    get_summary
)

from reports.report_insights import (
    generate_ai_insights
)

from reports.pdf_generator import (
    generate_pdf
)

from reports.excel_generator import (
    generate_excel
)

def build_reports(df):

    summary = get_summary(df)

    insights = generate_ai_insights(df)

    pdf_file = generate_pdf(
        summary,
        insights
    )

    excel_file = generate_excel(df)

    csv_file = (
        "reports/generated_reports/"
        "mental_health_report.csv"
    )

    df.to_csv(
        csv_file,
        index=False
    )

    text_file = (
        "reports/generated_reports/"
        "ai_summary.txt"
    )

    with open(
        text_file,
        "w"
    ) as file:

        file.write(insights)

    return {

        "pdf": pdf_file,

        "excel": excel_file,

        "csv": csv_file,

        "summary": text_file

    }
