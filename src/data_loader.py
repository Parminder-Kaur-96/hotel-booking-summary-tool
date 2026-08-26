from pathlib import Path
import pandas as pd


def load_booking_data(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    dataframe = pd.read_csv(file_path)

    if dataframe.empty:
        raise ValueError("The hotel booking dataset is empty.")

    return dataframe


def validate_dataframe(dataframe):
    expected_columns = [
        "Booking ID",
        "Hotel",
        "Is Canceled",
        "Lead Time",
        "Arrival Date",
        "Stays in Weekend Nights",
        "Stays in Week Nights",
        "Adults",
        "Children",
        "Meal",
        "Country",
        "Market Segment",
        "Distribution Channel",
        "Is Repeated Guest",
        "Reserved Room Type",
        "Assigned Room Type",
        "Deposit Type",
        "Customer Type",
        "Average Daily Rate",
        "Parking Spaces",
        "Special Requests",
        "Reservation Status",
        "Reservation Status Date",
    ]

    missing_columns = [
        column for column in expected_columns
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Dataset is missing expected columns: {missing_columns}"
        )

    return True