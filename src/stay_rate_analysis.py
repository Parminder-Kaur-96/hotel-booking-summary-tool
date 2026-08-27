"""Reusable stay and rate analysis functions for the Hotel Booking Summary Tool."""
import pandas as pd

def calculate_total_stay_length(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the total number of nights for each booking.

    Total stay length is calculated as:
    weekend nights + week nights.
    """
    return df["Stays in Weekend Nights"] + df["Stays in Week Nights"]