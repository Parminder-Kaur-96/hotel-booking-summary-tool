import pandas as pd

from src.summary import (
    create_consolidated_summary,
    format_summary,
)


def create_test_dataframe():
    return pd.DataFrame(
        {
            "Hotel": [
                "City Hotel",
                "Resort Hotel",
                "City Hotel",
                "Resort Hotel",
            ],
            "Market Segment": [
                "Online TA",
                "Direct",
                "Online TA",
                "Groups",
            ],
            "Is Canceled": [0, 1, 0, 1],
            "Stays in Weekend Nights": [1, 2, 0, 1],
            "Stays in Week Nights": [2, 3, 1, 2],
            "Average Daily Rate": [
                100.0,
                150.0,
                120.0,
                200.0,
            ],
        }
    )


def test_create_consolidated_summary():
    df = create_test_dataframe()

    summary = create_consolidated_summary(df)

    assert "cancellation" in summary
    assert "hotel" in summary
    assert "market_segment" in summary
    assert "stay_and_rate" in summary


def test_consolidated_cancellation_summary():
    df = create_test_dataframe()

    summary = create_consolidated_summary(df)

    cancellation = summary["cancellation"]

    assert cancellation["total_bookings"] == 4
    assert cancellation["cancelled_bookings"] == 2
    assert cancellation["non_cancelled_bookings"] == 2
    assert cancellation["cancellation_rate"] == 0.5


def test_consolidated_hotel_summary():
    df = create_test_dataframe()

    summary = create_consolidated_summary(df)

    hotel_summary = summary["hotel"]

    assert hotel_summary["Booking Count"].sum() == 4


def test_consolidated_market_segment_summary():
    df = create_test_dataframe()

    summary = create_consolidated_summary(df)

    market_summary = summary["market_segment"]

    assert market_summary["Booking Count"].sum() == 4


def test_consolidated_stay_and_rate_summary():
    df = create_test_dataframe()

    summary = create_consolidated_summary(df)

    stay_rate = summary["stay_and_rate"]

    assert stay_rate["stay_statistics"]["total_bookings"] == 4
    assert stay_rate["adr_summary"]["average_adr"] == 142.5


def test_format_summary():
    df = create_test_dataframe()

    summary = create_consolidated_summary(df)
    report = format_summary(summary)

    assert "HOTEL BOOKING SUMMARY REPORT" in report
    assert "CANCELLATION SUMMARY" in report
    assert "HOTEL SUMMARY" in report
    assert "MARKET SEGMENT SUMMARY" in report
    assert "STAY INSIGHTS" in report
    assert "RATE INSIGHTS" in report