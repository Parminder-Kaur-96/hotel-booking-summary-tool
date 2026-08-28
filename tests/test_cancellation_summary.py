import pandas as pd

from src.cancellation_summary import cancellation_summary


def test_cancellation_summary():
    data = {
        "Is Canceled": [0, 1, 0, 1, 0]
    }

    df = pd.DataFrame(data)

    result = cancellation_summary(df)

    assert result["total_bookings"] == 5
    assert result["cancelled_bookings"] == 2
    assert result["non_cancelled_bookings"] == 3
    assert result["cancellation_rate"] == 0.4


def test_all_bookings_cancelled():
    data = {
        "Is Canceled": [1, 1, 1]
    }

    df = pd.DataFrame(data)

    result = cancellation_summary(df)

    assert result["total_bookings"] == 3
    assert result["cancelled_bookings"] == 3
    assert result["non_cancelled_bookings"] == 0
    assert result["cancellation_rate"] == 1.0


def test_no_bookings_cancelled():
    data = {
        "Is Canceled": [0, 0, 0]
    }

    df = pd.DataFrame(data)

    result = cancellation_summary(df)

    assert result["total_bookings"] == 3
    assert result["cancelled_bookings"] == 0
    assert result["non_cancelled_bookings"] == 3
    assert result["cancellation_rate"] == 0.0