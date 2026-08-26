import pandas as pd
from src.booking_analysis import summarize_by_hotel
def test_summarize_by_hotel():
    df = pd.DataFrame(
        {
            "Hotel": [
                "City Hotel",
                "City Hotel",
                "Resort Hotel",
            ]
        }
    )

    result = summarize_by_hotel(df)

    assert result.loc[0, "Hotel"] == "City Hotel"
    assert result.loc[0, "Booking Count"] == 2
    assert result.loc[1, "Hotel"] == "Resort Hotel"
    assert result.loc[1, "Booking Count"] == 1

import pandas as pd

from src.booking_analysis import (
    summarize_by_hotel,
    summarize_by_market_segment,
)


def test_summarize_by_hotel():
    df = pd.DataFrame(
        {
            "Hotel": [
                "City Hotel",
                "City Hotel",
                "Resort Hotel",
            ]
        }
    )

    result = summarize_by_hotel(df)

    assert result.loc[0, "Hotel"] == "City Hotel"
    assert result.loc[0, "Booking Count"] == 2
    assert result.loc[1, "Hotel"] == "Resort Hotel"
    assert result.loc[1, "Booking Count"] == 1


def test_summarize_by_market_segment():
    df = pd.DataFrame(
        {
            "Market Segment": [
                "Online TA",
                "Online TA",
                "Direct",
                "Groups",
            ]
        }
    )

    result = summarize_by_market_segment(df)

    assert result.loc[0, "Market Segment"] == "Online TA"
    assert result.loc[0, "Booking Count"] == 2
    assert result["Booking Count"].sum() == 4
