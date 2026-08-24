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
