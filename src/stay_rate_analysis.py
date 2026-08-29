"""Reusable stay and rate analysis functions for the Hotel Booking Summary Tool."""

import pandas as pd


def validate_required_columns(
    df: pd.DataFrame, required_columns: list[str]
) -> None:
    """
    Validate that the required columns exist in the DataFrame.
    """
    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )


def calculate_total_stay_length(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the total number of nights for each booking.

    Total stay length is calculated as:
    weekend nights + week nights.
    """
    validate_required_columns(
        df,
        ["Stays in Weekend Nights", "Stays in Week Nights"],
    )
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


def summarize_adr(df: pd.DataFrame) -> dict:
    """
    Generate summary statistics for Average Daily Rate (ADR).
    """
    validate_required_columns(df, ["Average Daily Rate"])
    adr = df["Average Daily Rate"]

    return {
        "average_adr": adr.mean(),
        "minimum_adr": adr.min(),
        "maximum_adr": adr.max(),
    }


def summarize_stay_and_rate(df: pd.DataFrame) -> dict:
    """ 
    Generate a combined stay and rate summary.
    """
    return {
        "stay_statistics": summarize_stay_statistics(df),
        "adr_summary": summarize_adr(df),
    }
