# budget/data_model.py

from typing import List
import pandas as pd

from .config import DEFAULT_MONTHS, DEFAULT_CATEGORIES


def enforce_month_order(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure the 'month' column is ordered Jan -> Dec, not alphabetically.
    """
    df = df.copy()
    df["month"] = pd.Categorical(
        df["month"], categories=DEFAULT_MONTHS, ordered=True
    )
    df = df.sort_values("month")
    return df


def create_default_budget(months: List[str] = None) -> pd.DataFrame:
    """
    Create a default budget DataFrame with all categories and months initialised to 0.

    Columns: ["group", "item", "type", "month", "amount"]
    """
    if months is None:
        months = DEFAULT_MONTHS

    records = []
    for group, item, cat_type in DEFAULT_CATEGORIES:
        for month in months:
            records.append(
                {
                    "group": group,
                    "item": item,
                    "type": cat_type,
                    "month": month,
                    "amount": 0.0,
                }
            )

    df = pd.DataFrame(records)
    df = enforce_month_order(df)
    return df


def update_amount(
    df: pd.DataFrame,
    group: str,
    item: str,
    month: str,
    amount: float,
) -> pd.DataFrame:
    """
    Return a new DataFrame with the specified cell updated.
    """
    mask = (
        (df["group"] == group)
        & (df["item"] == item)
        & (df["month"] == month)
    )

    new_df = df.copy()
    new_df.loc[mask, "amount"] = amount
    return new_df


def copy_month_to_all(df: pd.DataFrame, source_month: str) -> pd.DataFrame:
    """
    Copy all values from source_month to every month for each (group, item).

    This assumes the same categories exist for all months.
    """
    new_df = df.copy()
    src_df = new_df[new_df["month"] == source_month]

    for _, row in src_df.iterrows():
        group = row["group"]
        item = row["item"]
        value = row["amount"]

        mask = (
            (new_df["group"] == group)
            & (new_df["item"] == item)
        )
        new_df.loc[mask, "amount"] = value

    return new_df
