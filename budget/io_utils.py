from pathlib import Path
from typing import Union

import pandas as pd

from .config import DEFAULT_MONTHS, DEFAULT_CATEGORIES
from .data_model import create_default_budget


def load_budget_from_excel(path: Union[str, Path]) -> pd.DataFrame:
    """
    TODO: Parse your existing spreadsheet structure into our standard DataFrame shape.

    For now this is just a stub returning a fresh default budget.
    """
    # Later: read Excel, map rows/columns to (group, item, type, month, amount)
    return create_default_budget()


def export_budget_to_excel(df: pd.DataFrame, path: Union[str, Path]) -> None:
    """
    Export current budget to Excel in a simple tabular format.
    """
    path = Path(path)
    df.to_excel(path, index=False)
