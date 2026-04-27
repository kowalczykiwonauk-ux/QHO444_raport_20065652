# # Module Code: 	QHO444 Software artifact with report
#
# Data processing task are hande in this  module.
#It will primarily include functions that take the full dataset as input and apply the required operations to produce the final output in the appropriate format.
#Most parts of the project are expected to rely on functions defined within this module

import csv
from collections import defaultdict


def load_data(filepath):
    """
    Read the CSV file at filepath and return a list of row dictionaries.
    Each dictionary maps column names to their string (or cast) values.
    The Rating column is converted to int; all others remain strings.
    """
    dataset = []
    with open(filepath, newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["Rating"] = int(row["Rating"])
            dataset.append(dict(row))
    return dataset


def get_unique_parks(dataset):
    """Return a sorted list of unique park names found in the dataset."""
    return sorted({row["Branch"] for row in dataset})


def get_reviews_for_park(dataset, park):
    """Return all rows where the Branch matches park (case-insensitive)."""
    park_lower = park.lower()
    return [row for row in dataset if row["Branch"].lower() == park_lower]


def get_review_count_by_location(dataset, park, location):
    """Return the number of reviews for park from a specific reviewer location."""
    park_lower = park.lower()
    location_lower = location.lower()
    return sum(
        1
        for row in dataset
        if row["Branch"].lower() == park_lower
        and row["Reviewer_Location"].lower() == location_lower
    )


def get_average_rating(dataset, park, year):
    """
    Return the average rating (float) for a park in a given year.
    Year_Month values are formatted as 'YYYY-M' or 'YYYY-MM'.
    Returns None if no matching reviews are found.
    """
    park_lower = park.lower()
    ratings = [
        row["Rating"]
        for row in dataset
        if row["Branch"].lower() == park_lower
        and row["Year_Month"].split("-")[0] == str(year)
        and row["Year_Month"].split("-")[0].isdigit()
    ]
    return sum(ratings) / len(ratings) if ratings else None


def get_avg_rating_per_location_per_park(dataset):
    """
    Return a nested dict: {park: {location: average_rating}}.
    For every park, calculate the average rating for every location that reviewed it.
    """
    # Accumulate totals: {park: {location: [sum, count]}}
    totals = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for row in dataset:
        park = row["Branch"]
        location = row["Reviewer_Location"]
        totals[park][location][0] += row["Rating"]
        totals[park][location][1] += 1

    result = {}
    for park, locations in totals.items():
        result[park] = {
            loc: values[0] / values[1]
            for loc, values in locations.items()
        }
    return result


def get_review_counts_per_park(dataset):
    """Return a dict mapping each park to its total number of reviews."""
    counts = defaultdict(int)
    for row in dataset:
        counts[row["Branch"]] += 1
    return dict(counts)


def get_top_locations_by_avg_rating(dataset, park, top_n=10):
    """
    For a given park, return the top_n locations with the highest average rating.
    Returns a list of (location, average_rating) tuples, sorted descending.
    """
    park_data = defaultdict(lambda: [0, 0])
    for row in dataset:
        if row["Branch"] == park:
            loc = row["Reviewer_Location"]
            park_data[loc][0] += row["Rating"]
            park_data[loc][1] += 1

    averages = [
        (loc, values[0] / values[1])
        for loc, values in park_data.items()
    ]
    averages.sort(key=lambda x: -x[1])
    return averages[:top_n]


def get_avg_rating_by_month(dataset, park):
    """
    For a given park, return a list of (month_number, average_rating) tuples
    ordered by calendar month (1–12).  Months with no reviews are omitted.
    """
    month_totals = defaultdict(lambda: [0, 0])
    for row in dataset:
        if row["Branch"] == park:
            parts = row["Year_Month"].split("-")
            if len(parts) < 2 or not parts[1].isdigit():
                continue
            month = int(parts[1])
            month_totals[month][0] += row["Rating"]
            month_totals[month][1] += 1

    return sorted(
        [(month, values[0] / values[1]) for month, values in month_totals.items()],
        key=lambda x: x[0],
    )


def get_park_summary(dataset):
    """
    Return a dict mapping each park to a summary dict containing:
      - num_reviews      (int)
      - num_positive     (int)  ratings >= 4 count as positive
      - avg_rating       (float)
      - num_countries    (int)  distinct Reviewer_Location values
    """
    accumulator = defaultdict(
        lambda: {"ratings": [], "locations": set()}
    )
    for row in dataset:
        park = row["Branch"]
        accumulator[park]["ratings"].append(row["Rating"])
        accumulator[park]["locations"].add(row["Reviewer_Location"])

    summary = {}
    for park, data in accumulator.items():
        ratings = data["ratings"]
        summary[park] = {
            "num_reviews": len(ratings),
            "num_positive": sum(1 for r in ratings if r >= 4),
            "avg_rating": round(sum(ratings) / len(ratings), 2),
            "num_countries": len(data["locations"]),
        }
    return summary
