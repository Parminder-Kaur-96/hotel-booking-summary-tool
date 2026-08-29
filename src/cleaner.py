import os
import numpy as np
import pandas as pd


def load_data(file_path: str = "data/hotel_bookings.csv") -> pd.DataFrame:
  """Loads a CSV file from the specified path (defaults to 'data/hotel_bookings.csv')."""
  try:
    df = pd.read_csv(file_path)
    print(f"File successfully loaded from '{file_path}'. Records: {len(df)}")
    return df
  except Exception as e:
    print(f"Error loading file '{file_path}': {e}")
    raise e


def save_data(
    df: pd.DataFrame, output_path: str = "data/hotel_bookings_cleaned.csv"
) -> None:
  """Saves the DataFrame to a CSV file."""
  os.makedirs(os.path.dirname(output_path), exist_ok=True)
  df.to_csv(output_path, index=False)
  print(f"Cleaned data successfully saved to '{output_path}'.")


def standardize_text_columns(
    df: pd.DataFrame, target_cols: list = None
) -> pd.DataFrame:
  """Strips leading/trailing whitespace and applies Title Case to text columns.

  If no target columns are provided, it automatically selects all object/string
  columns.
  """
  df_clean = df.copy()

  # Automatically detect text columns if not explicitly provided
  if target_cols is None:
    target_cols = df_clean.select_dtypes(
        include=["object", "string"]
    ).columns.tolist()

  for col in target_cols:
    if col in df_clean.columns:
      mask = df_clean[col].notna()
      df_clean.loc[mask, col] = (
          df_clean.loc[mask, col].astype(str).str.strip().str.title()
      )
  return df_clean


def clean_numeric_columns(df: pd.DataFrame, numeric_cols: list) -> pd.DataFrame:
  """Removes non-numeric characters (e.g., '$', 'USD', 'guests') from numeric columns

  and converts valid values to int/float.
  """
  df_clean = df.copy()
  for col in numeric_cols:
    if col in df_clean.columns:
      s = df_clean[col].astype(str).str.replace(r"[^0-9.]", "", regex=True)
      df_clean[col] = pd.to_numeric(s, errors="coerce")
  return df_clean


def clean_dataset(
    df: pd.DataFrame, expected_numeric: list = None
) -> pd.DataFrame:
  """Complete data cleaning pipeline:

  1. Removes exact duplicates.
  2. Cleans text and standardizes casing across all categorical/text columns.
  3. Cleans and converts malformed numeric columns.
  """
  # 1. Drop exact duplicate rows
  df_clean = df.drop_duplicates().copy()

  # 2. Automatic text cleaning across text columns
  df_clean = standardize_text_columns(df_clean)

  # 3. Clean numeric columns containing text formatting issues
  if expected_numeric:
    df_clean = clean_numeric_columns(df_clean, expected_numeric)

  return df_clean


if __name__ == "__main__":
  INPUT_PATH = "data/hotel_bookings.csv"
  OUTPUT_PATH = "data/hotel_bookings_cleaned.csv"

  numeric_cols = [
      "Lead Time",
      "Stays in Weekend Nights",
      "Stays in Week Nights",
      "Adults",
      "Children",
      "Average Daily Rate",
      "Parking Spaces",
  ]

  df_raw = load_data(INPUT_PATH)
  df_cleaned = clean_dataset(df_raw, expected_numeric=numeric_cols)
  save_data(df_cleaned, OUTPUT_PATH)