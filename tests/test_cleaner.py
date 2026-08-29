import os
from pathlib import Path
import sys
import tempfile
import unittest
import numpy as np
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.cleaner import (
    clean_dataset,
    clean_numeric_columns,
    load_data,
    save_data,
    standardize_text_columns,
)


class TestCleaner(unittest.TestCase):

  def setUp(self):
    """Dummy dataset with multi-column spacing and casing inconsistencies."""
    self.raw_data = pd.DataFrame({
        "Hotel": ["City Hotel", " Resort Hotel", "CITY HOTEL", "city hotel"],
        "Meal": ["  BB", "bb ", "Bb", "FB "],
        "Market Segment": ["Direct", " direct", "DIRECT ", "Direct"],
        "Adults": ["2", "1 guests", " 2 ", "unknown"],
        "Average Daily Rate": ["$ 90", "100.5", "USD 85.00", "0"],
    })

  def test_load_and_save_csv(self):
    """Verify loading and saving functionality for CSV files."""
    with tempfile.TemporaryDirectory() as tmp_dir:
      temp_csv = os.path.join(tmp_dir, "hotel_bookings.csv")
      temp_out = os.path.join(tmp_dir, "hotel_bookings_cleaned.csv")

      # Create temporary test CSV file
      self.raw_data.to_csv(temp_csv, index=False)

      # Test load from custom path
      loaded_df = load_data(temp_csv)
      self.assertEqual(len(loaded_df), len(self.raw_data))

      # Test save
      save_data(loaded_df, temp_out)
      self.assertTrue(os.path.exists(temp_out))

  def test_standardize_text_columns_auto_detect(self):
    """Verify automatic detection and cleaning of all text columns."""
    cleaned_df = standardize_text_columns(self.raw_data)

    # Validate Hotel column
    self.assertCountEqual(
        cleaned_df["Hotel"].unique(), ["City Hotel", "Resort Hotel"]
    )

    # Validate Meal column
    self.assertCountEqual(cleaned_df["Meal"].unique(), ["Bb", "Fb"])

    # Validate Market Segment column
    self.assertCountEqual(cleaned_df["Market Segment"].unique(), ["Direct"])

  def test_clean_numeric_columns(self):
    """Verify extraction and conversion of numeric values."""
    cleaned_df = clean_numeric_columns(
        self.raw_data, ["Adults", "Average Daily Rate"]
    )

    self.assertEqual(cleaned_df["Adults"].iloc[1], 1.0)
    self.assertTrue(np.isnan(cleaned_df["Adults"].iloc[3]))
    self.assertEqual(cleaned_df["Average Daily Rate"].iloc[0], 90.0)

  def test_clean_dataset_pipeline(self):
    """Verify complete pipeline execution on a DataFrame."""
    numeric_cols = ["Adults", "Average Daily Rate"]
    cleaned_df = clean_dataset(self.raw_data, expected_numeric=numeric_cols)

    self.assertEqual(len(cleaned_df["Meal"].unique()), 2)
    self.assertEqual(len(cleaned_df["Hotel"].unique()), 2)
    self.assertIsInstance(cleaned_df, pd.DataFrame)


if __name__ == "__main__":
  unittest.main()