# budget/charts.py

import pandas as pd
import streamlit as st


def show_monthly_summary_chart(summary_df: pd.DataFrame):
    """
    Display a simple chart of income vs expenses vs net by month as a line chart.
    """
    if summary_df.empty:
        st.info("No data to display yet.")
        return

    st.line_chart(
        summary_df.set_index("month")[["income", "expenses", "net"]]
    )


def show_group_breakdown_chart(group_df: pd.DataFrame):
    """
    Display a chart of totals by group for a single month.
    Expects columns: ["group", "total"]
    """
    if group_df.empty:
        st.info("No data to display yet.")
        return

    st.bar_chart(group_df.set_index("group")["total"])
