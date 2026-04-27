"""
This module implements the OOP-based data export feature (Section D).

Class hierarchy:

    DataExporter  (abstract base)
        └── TxtExporter
        └── CsvExporter
        └── JsonExporter

Each concrete exporter receives a park summary dict and writes it to a file
in its respective format.
"""

import csv
import json
import os
from abc import ABC, abstractmethod


class DataExporter(ABC):
    """
    Abstract base class for all park-data exporters.

    Subclasses must implement the `export` method to serialise the provided
    summary data to a specific file format.
    """

    def __init__(self, summary, output_dir="exports"):
        """
        Initialise the exporter with park summary data.

        ----------
        Parameters
        ----------
        summary : dict
            {park: {num_reviews, num_positive, avg_rating, num_countries}}
            as returned by process.get_park_summary().
        output_dir : str
            Directory in which output files will be saved.
        """
        self._summary = summary
        self._output_dir = output_dir
        os.makedirs(self._output_dir, exist_ok=True)

    @property
    def output_dir(self):
        """Return the output directory path."""
        return self._output_dir

    @abstractmethod
    def export(self, filename):
        """
        Serialise the park summary data and write it to a file.

        ----------
        Parameters
        ----------
        filename : str
            Base filename (without extension).

        -------
        Returns
        -------
        str
            Full path of the file that was written.
        """

    def _build_filepath(self, filename, extension):
        """Construct and return the full file path."""
        return os.path.join(self._output_dir, f"{filename}.{extension}")


class TxtExporter(DataExporter):
    """Export park summary data to a plain-text (.txt) file."""

    def export(self, filename="park_summary"):
        """Write summary data as formatted plain text."""
        filepath = self._build_filepath(filename, "txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Disneyland Park Summary Report\n")
            f.write("=" * 50 + "\n\n")
            for park, data in sorted(self._summary.items()):
                f.write(f"Park:              {park}\n")
                f.write(f"  Reviews:         {data['num_reviews']}\n")
                f.write(f"  Positive (>=4):  {data['num_positive']}\n")
                f.write(f"  Average Rating:  {data['avg_rating']:.2f}\n")
                f.write(f"  Countries:       {data['num_countries']}\n")
                f.write("-" * 50 + "\n")
        return filepath


class CsvExporter(DataExporter):
    """Export park summary data to a CSV (.csv) file."""

    FIELDS = ["Park", "Num_Reviews", "Num_Positive", "Avg_Rating", "Num_Countries"]

    def export(self, filename="park_summary"):
        """Write summary data as a CSV file with a header row."""
        filepath = self._build_filepath(filename, "csv")
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDS)
            writer.writeheader()
            for park, data in sorted(self._summary.items()):
                writer.writerow({
                    "Park": park,
                    "Num_Reviews": data["num_reviews"],
                    "Num_Positive": data["num_positive"],
                    "Avg_Rating": data["avg_rating"],
                    "Num_Countries": data["num_countries"],
                })
        return filepath


class JsonExporter(DataExporter):
    """Export park summary data to a JSON (.json) file."""

    def export(self, filename="park_summary"):
        """Write summary data as a formatted JSON file."""
        filepath = self._build_filepath(filename, "json")
        output = {}
        for park, data in sorted(self._summary.items()):
            output[park] = {
                "num_reviews": data["num_reviews"],
                "num_positive": data["num_positive"],
                "avg_rating": data["avg_rating"],
                "num_countries": data["num_countries"],
            }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)
        return filepath


def create_exporter(fmt, summary):
    """
    Factory function — return the correct DataExporter subclass for fmt.

    Parameters
    ----------
    fmt : str
        One of 'TXT', 'CSV', 'JSON' (case-insensitive).
    summary : dict
        Park summary data.

    Returns
    -------
    DataExporter
        Concrete exporter instance.

    Raises
    ------
    ValueError
        If fmt is not a recognised format string.
    """
    fmt_upper = fmt.upper()
    exporters = {
        "TXT": TxtExporter,
        "CSV": CsvExporter,
        "JSON": JsonExporter,
    }
    if fmt_upper not in exporters:
        raise ValueError(f"Unknown export format: {fmt}")
    return exporters[fmt_upper](summary)
