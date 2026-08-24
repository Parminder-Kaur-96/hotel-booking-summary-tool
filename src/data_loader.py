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
