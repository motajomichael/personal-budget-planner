# budget/calculations.py

import pandas as pd

from .config import DEFAULT_MONTHS


def get_month_totals(df: pd.DataFrame, month: str) -> dict:
    """
    Compute total income, total expenses and net for a given month.
    """
    month_df = df[df["month"] == month]

    income = month_df.loc[month_df["type"] == "income", "amount"].sum()
    expenses = month_df.loc[month_df["type"] == "expense", "amount"].sum()
    net = income - expenses

    return {
        "income": float(income),
        "expenses": float(expenses),
        "net": float(net),
    }


def get_monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate income, expenses and net for each month.

    Returns: columns ["month", "income", "expenses", "net"],
    ordered Jan -> Dec.
    """
    income_df = (
        df[df["type"] == "income"]
        .groupby("month")["amount"]
        .sum()
        .rename("income")
    )
    expenses_df = (
        df[df["type"] == "expense"]
        .groupby("month")["amount"]
        .sum()
        .rename("expenses")
    )

    summary = pd.concat([income_df, expenses_df], axis=1).fillna(0.0)
    summary["net"] = summary["income"] - summary["expenses"]
    summary = summary.reset_index()

    # enforce month order here too
    summary["month"] = pd.Categorical(
        summary["month"], categories=DEFAULT_MONTHS, ordered=True
    )
    summary = summary.sort_values("month").reset_index(drop=True)

    return summary


def get_group_totals_for_month(df: pd.DataFrame, month: str) -> pd.DataFrame:
    """
    Return total amount per group for a given month.
    Columns: ["group", "total"]
    """
    month_df = df[df["month"] == month]
    grouped = month_df.groupby("group")["amount"].sum().reset_index()
    grouped = grouped.rename(columns={"amount": "total"})
    return grouped


def projected_end_balance(starting_balance: float, net: float) -> float:
    """
    Simple projection: starting balance + net.
    """
    return float(starting_balance + net)
