"""Main entry point for the Hotel Booking Summary Tool."""

from src.data_loader import load_booking_data, validate_dataframe
from src.cleaner import clean_dataset
from src.summary import create_consolidated_summary, format_summary


DATASET_PATH = "data/hotel_bookings.csv"


def main():
    """Run the complete hotel booking analysis workflow."""

    print("Loading hotel booking dataset...")

    # Step 1: Load dataset
    df = load_booking_data(DATASET_PATH)

    # Step 2: Validate dataset structure
    validate_dataframe(df)

    # Step 3: Clean and prepare data
    numeric_columns = [
        "Lead Time",
        "Stays in Weekend Nights",
        "Stays in Week Nights",
        "Adults",
        "Children",
        "Average Daily Rate",
        "Parking Spaces",
    ]

    df = clean_dataset(
        df,
        expected_numeric=numeric_columns,
    )

    # Step 4: Generate consolidated summary
    summary = create_consolidated_summary(df)

    # Step 5: Format and display final output
    report = format_summary(summary)

    print(report)


if __name__ == "__main__":
    main()