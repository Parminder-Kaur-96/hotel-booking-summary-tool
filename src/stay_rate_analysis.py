"""Reusable stay and rate analysis functions for the Hotel Booking Summary Tool."""
import pandas as pd

def calculate_total_stay_length(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the total number of nights for each booking.

    Total stay length is calculated as:
    weekend nights + week nights.
    """
    return df["Stays in Weekend Nights"] + df["Stays in Week Nights"]

def summarize_stay_statistics(df: pd.DataFrame) -> dict:
    """
    Generate summary statistics for booking stay lengths.
    """
    total_stay = calculate_total_stay_length(df)

    return {
        "total_bookings": len(df),
        "average_stay_nights": total_stay.mean(),
        "minimum_stay_nights": total_stay.min(),
        "maximum_stay_nights": total_stay.max(),
    }   
