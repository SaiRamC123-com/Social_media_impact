import streamlit as st

from utils.data_loader import load_data

from reports.report_builder import (
    build_reports
)

df = load_data()

st.title("📄 Report Center")

st.markdown("""
Generate PDF, Excel, CSV and
AI-powered Summary Reports.
""")

if st.button(
    "Generate Complete Report"
):

    files = build_reports(df)

    st.success(
        "Reports Generated Successfully"
    )

    st.write(files)

st.divider()

st.subheader(
    "Dataset Preview"
)

st.dataframe(df.head(20))
