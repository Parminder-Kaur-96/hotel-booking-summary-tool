import pandas as pd


def cancellation_summary(df):
    """
    Calculate booking cancellation statistics.

    Returns:
        dict: Total bookings, cancelled bookings,
              non-cancelled bookings, and cancellation rate.
    """

    total_bookings = len(df)

    cancelled_bookings = (df["Is Canceled"] == 1).sum()

    non_cancelled_bookings = (df["Is Canceled"] == 0).sum()

    cancellation_rate = cancelled_bookings / total_bookings

    return {
        "total_bookings": total_bookings,
        "cancelled_bookings": cancelled_bookings,
        "non_cancelled_bookings": non_cancelled_bookings,
        "cancellation_rate": cancellation_rate
    }


if __name__ == "__main__":
    df = pd.read_csv("data/hotel_bookings.csv")

    summary = cancellation_summary(df)

    print(f"Total bookings: {summary['total_bookings']}")
    print(f"Cancelled bookings: {summary['cancelled_bookings']}")
    print(f"Non-cancelled bookings: {summary['non_cancelled_bookings']}")
    print(f"Cancellation rate: {summary['cancellation_rate']:.2%}")