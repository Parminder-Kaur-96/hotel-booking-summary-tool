"""Reusable booking analysis functions for the Hotel Booking Summary Tool."""

import pandas as pd


def summarize_by_hotel(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return the number of bookings grouped by hotel type.

    Parameters
    ----------
    df : pandas.DataFrame
        Hotel booking dataset.

    Returns
    -------
    pandas.DataFrame
        Summary containing hotel type and booking count.
    """
    if "Hotel" not in df.columns:
        raise ValueError("Required column 'Hotel' was not found in the dataset.")

    summary = (
        df.groupby("Hotel", dropna=False)
        .size()
        .reset_index(name="Booking Count")
        .sort_values("Booking Count", ascending=False)
        .reset_index(drop=True)
    )

    return summary
