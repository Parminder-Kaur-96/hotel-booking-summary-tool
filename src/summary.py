import pandas as pd

from src.booking_analysis import (
    summarize_by_hotel,
    summarize_by_market_segment,
)

from src.cancellation_summary import cancellation_summary
from src.stay_rate_analysis import summarize_stay_and_rate

def create_consolidated_summary(df: pd.DataFrame) -> dict:
    """
    Generate a consolidated summary using all completed analysis functions.

    Parameters
    ----------
    df : pandas.DataFrame
        Prepared hotel booking dataset.

    Returns
    -------
    dict
        Dictionary containing cancellation, hotel, market segment,
        stay, and ADR summaries.
    """

    return {
        "cancellation": cancellation_summary(df),
        "hotel": summarize_by_hotel(df),
        "market_segment": summarize_by_market_segment(df),
        "stay_and_rate": summarize_stay_and_rate(df),
    }

def format_summary(summary: dict) -> str:
    """
    Format the consolidated summary as a readable text report.
    """

    cancellation = summary["cancellation"]
    hotel = summary["hotel"]
    market_segment = summary["market_segment"]
    stay_rate = summary["stay_and_rate"]

    stay = stay_rate["stay_statistics"]
    adr = stay_rate["adr_summary"]

    lines = []

    lines.append("=" * 60)
    lines.append("       HOTEL BOOKING SUMMARY REPORT")
    lines.append("=" * 60)

    lines.append("")
    lines.append("DATASET")
    lines.append("-" * 60)
    lines.append(
        f"Total bookings: {cancellation['total_bookings']:,}"
    )

    lines.append("")
    lines.append("CANCELLATION SUMMARY")
    lines.append("-" * 60)
    lines.append(
        f"Total bookings:       {cancellation['total_bookings']:,}"
    )
    lines.append(
        f"Cancelled bookings:   {cancellation['cancelled_bookings']:,}"
    )
    lines.append(
        f"Non-cancelled:        {cancellation['non_cancelled_bookings']:,}"
    )
    lines.append(
        f"Cancellation rate:    {cancellation['cancellation_rate']:.2%}"
    )

    lines.append("")
    lines.append("HOTEL SUMMARY")
    lines.append("-" * 60)

    for _, row in hotel.iterrows():
        lines.append(
            f"{row['Hotel']}: {row['Booking Count']:,}"
        )

    lines.append("")
    lines.append("MARKET SEGMENT SUMMARY")
    lines.append("-" * 60)

    for _, row in market_segment.iterrows():
        lines.append(
            f"{row['Market Segment']}: {row['Booking Count']:,}"
        )

    lines.append("")
    lines.append("STAY INSIGHTS")
    lines.append("-" * 60)
    lines.append(
        f"Average stay: {stay['average_stay_nights']:.2f} nights"
    )
    lines.append(
        f"Minimum stay: {stay['minimum_stay_nights']:.0f} nights"
    )
    lines.append(
        f"Maximum stay: {stay['maximum_stay_nights']:.0f} nights"
    )

    lines.append("")
    lines.append("RATE INSIGHTS")
    lines.append("-" * 60)
    lines.append(
        f"Average ADR: ${adr['average_adr']:.2f}"
    )
    lines.append(
        f"Minimum ADR: ${adr['minimum_adr']:.2f}"
    )
    lines.append(
        f"Maximum ADR: ${adr['maximum_adr']:.2f}"
    )

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)