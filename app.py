# app.py

import streamlit as st

from budget.config import DEFAULT_MONTHS
from budget.data_model import (
    create_default_budget,
    update_amount,
    copy_month_to_all,
)
from budget.calculations import (
    get_month_totals,
    get_monthly_summary,
    get_group_totals_for_month,
    projected_end_balance,
)
from budget.charts import (
    show_monthly_summary_chart,
    show_group_breakdown_chart,
)


def init_session_state():
    """
    Make sure all required session_state keys exist.
    This MUST be called before any use of st.session_state.budget_df.
    """
    if "budget_df" not in st.session_state:
        st.session_state.budget_df = create_default_budget()
    if "starting_balance" not in st.session_state:
        st.session_state.starting_balance = 0.0
    if "selected_month" not in st.session_state:
        st.session_state.selected_month = DEFAULT_MONTHS[0]


def on_amount_change(group: str, item: str, month: str, key: str):
    """
    Callback for when a category amount changes.
    Reads the new value from st.session_state[key] and updates budget_df.
    This runs BEFORE the rest of the script, so summaries see fresh data.
    """
    new_value = float(st.session_state[key])
    st.session_state.budget_df = update_amount(
        st.session_state.budget_df,
        group=group,
        item=item,
        month=month,
        amount=new_value,
    )


def sidebar_controls():
    with st.sidebar:
        st.header("Controls")

        month = st.selectbox(
            "Select month",
            options=DEFAULT_MONTHS,
            index=DEFAULT_MONTHS.index(st.session_state.selected_month),
        )
        st.session_state.selected_month = month

        starting_balance = st.number_input(
            "Starting balance",
            value=float(st.session_state.starting_balance),
            step=100.0,
        )
        st.session_state.starting_balance = starting_balance

        st.markdown("---")
        st.caption("Adjust your month and starting balance here.")

        st.markdown("---")
        st.subheader("Copy values")
        if st.button("Copy this month to all months"):
            st.session_state.budget_df = copy_month_to_all(
                st.session_state.budget_df,
                st.session_state.selected_month,
            )
            st.success(
                f"Values from {st.session_state.selected_month} copied to all months."
            )


def render_summary_cards():
    df = st.session_state.budget_df
    month = st.session_state.selected_month
    starting_balance = st.session_state.starting_balance

    totals = get_month_totals(df, month)
    end_balance = projected_end_balance(starting_balance, totals["net"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Income", f"{totals['income']:,.0f}")
    col2.metric("Total Expenses", f"{totals['expenses']:,.0f}")
    col3.metric("Net (Income - Expenses)", f"{totals['net']:,.0f}")
    col4.metric("Projected End Balance", f"{end_balance:,.0f}")


def render_category_editor():
    st.subheader("Edit categories for selected month")

    df = st.session_state.budget_df
    month = st.session_state.selected_month

    month_df = df[df["month"] == month].copy()
    groups = month_df["group"].unique()

    for group in groups:
        group_df = month_df[month_df["group"] == group]

        with st.expander(group, expanded=(group in ["Income", "Home Expenses"])):
            for _, row in group_df.iterrows():
                item = row["item"]
                current_value = float(row["amount"])

                # unique key per (group, item, month)
                key = f"amount|{group}|{item}|{month}"

                # number_input now uses on_change callback
                st.number_input(
                    item,
                    value=current_value,
                    step=50.0,
                    key=key,
                    on_change=on_amount_change,
                    kwargs={
                        "group": group,
                        "item": item,
                        "month": month,
                        "key": key,
                    },
                )


def render_tabs():
    df = st.session_state.budget_df
    month = st.session_state.selected_month

    tab_summary, tab_groups, tab_raw = st.tabs(
        ["Summary", "Group breakdown", "Raw data"]
    )

    with tab_summary:
        st.subheader("Monthly overview")
        summary_df = get_monthly_summary(df)
        show_monthly_summary_chart(summary_df)
        st.dataframe(summary_df, use_container_width=True)

    with tab_groups:
        st.subheader(f"Expenses by group - {month}")
        group_totals = get_group_totals_for_month(df, month)
        show_group_breakdown_chart(group_totals)
        st.dataframe(group_totals, use_container_width=True)

    with tab_raw:
        st.subheader("Raw budget data (power users)")
        st.dataframe(df, use_container_width=True)


def main():
    st.set_page_config(
        page_title="Personal Budget Planner",
        page_icon=None,
        layout="wide",
    )

    init_session_state()
    sidebar_controls()

    st.title("Personal Budget Planner")

    # Now that callbacks keep budget_df up-to-date,
    # these will see the latest values immediately after you tab out.
    render_summary_cards()
    render_category_editor()
    render_tabs()


if __name__ == "__main__":
    main()
