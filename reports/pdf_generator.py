from fpdf import FPDF

def generate_pdf(summary, insights):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        18
    )

    pdf.cell(
        200,
        10,
        "Social Media Impact Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        "",
        12
    )

    for key,value in summary.items():

        pdf.cell(
            200,
            10,
            f"{key}: {value}",
            ln=True
        )

    pdf.ln(10)

    pdf.multi_cell(
        0,
        8,
        insights
    )

    path = (
        "reports/generated_reports/"
        "mental_health_report.pdf"
    )

    pdf.output(path)

    return path
