import pandas as pd
import pytest

from src.stay_rate_analysis import (
    calculate_total_stay_length,
    summarize_stay_statistics,
    summarize_adr,
    summarize_stay_and_rate,
)


def test_calculate_total_stay_length():
    df = pd.DataFrame(
        {
            "Stays in Weekend Nights": [2, 1, 0],
            "Stays in Week Nights": [3, 4, 2],
        }
    )

    result = calculate_total_stay_length(df)

    assert result.tolist() == [5, 5, 2]


def test_summarize_stay_statistics():
    df = pd.DataFrame(
        {
            "Stays in Weekend Nights": [2, 1, 0],
            "Stays in Week Nights": [3, 4, 2],
        }
    )

    result = summarize_stay_statistics(df)

    assert result["total_bookings"] == 3
    assert result["average_stay_nights"] == 4.0
    assert result["minimum_stay_nights"] == 2
    assert result["maximum_stay_nights"] == 5


def test_summarize_adr():
    df = pd.DataFrame(
        {
            "Average Daily Rate": [100.0, 150.0, 200.0],
        }
    )

    result = summarize_adr(df)

    assert result["average_adr"] == 150.0
    assert result["minimum_adr"] == 100.0
    assert result["maximum_adr"] == 200.0


def test_summarize_stay_and_rate():
    df = pd.DataFrame(
        {
            "Stays in Weekend Nights": [2, 1, 0],
            "Stays in Week Nights": [3, 4, 2],
            "Average Daily Rate": [100.0, 150.0, 200.0],
        }
    )

    result = summarize_stay_and_rate(df)

    assert result["stay_statistics"]["total_bookings"] == 3
    assert result["stay_statistics"]["average_stay_nights"] == 4.0
    assert result["adr_summary"]["average_adr"] == 150.0


def test_missing_stay_column_raises_error():
    df = pd.DataFrame(
        {
            "Stays in Weekend Nights": [1, 2],
        }
    )

    with pytest.raises(ValueError):
        calculate_total_stay_length(df)


def test_missing_adr_column_raises_error():
    df = pd.DataFrame(
        {
            "Other Column": [100, 200],
        }
    )

    with pytest.raises(ValueError):
        summarize_adr(df)

