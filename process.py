# # Module Code: 	QHO444 Software artifact with report
#
# data processing task are hande in this  module.
#It will primarily include functions that take the full dataset as input and apply the required operations to produce the final output in the appropriate format.
#Most parts of the project are expected to rely on functions defined within this module

import csv
from collections import defaultdict

def lod_data(filepath):
    """
    Read the cvs file at filepath and return a list of row  dictionaries.
    Each dictionary maps column names to their string (or cast) values.
    The Rating colum is covered to int; all others remain strings.
    """

    dataset = []
    with open(filepath, newline="", encoding="utf - 8 -sig") as cvs_file:
        reader = cvs.DictReader (csv_file)
        for row in reader:
            dataset.append (dict(row))
    return dataset

def get_unique_parks(dataset):
    """ Return a sorted list of unique park names found in the dataset. """
    return sorted({row["Branch"] for row in dataset})


def get_reviews_for_park(dataset, park):
    """ Return  all rows where the Branch matches park (case-insensitive). """
    park_lower = park.lower()
    return [row for row in dataset if row["Branch"] == park_lower]

def get review_count_by_location(dataset, park, location)
    """ Return the numbers of reviews for park from a specific reviewer location"""
    park_lower = park.lower()
    location_lower = location.lower()
    return sum(
        1 for row in dataset
        if row["Branch"].lower() == location_lower)

def gre_average_rating(dataset, park, year):
    """
    Return the average rating (float) for a prk in a give year.
    Year_Month values are formatted as 'YYYY-M' or 'YYY-MM'.
    Return None if there is no matching reviews  are found.
    """
    park_lower =park.lower()
    ratings = [
        row["Rating"]
        for row in dataset
        if row["Branch"].lower() == park_lower
        and row["Yer_Month"].split("-")[0] == str(year)
        and row["Yer_Month"].split("-")[0].isdigit()
    ]
    return sum(ratings) / len(ratings) if ratings else None

def get_avg_rating_per_location_per_park(dataset):
    """Return a nested dict:{park: {location: average-rating}}.
    For every park, calculate teh average rating for every location that reviewed it
    """
    #Accumulate tots: {park: {loction : [sum,count]}}
    totals = defaultdict(lambda:defaultdict(lambda: [0, 0]))
    for row in dataset:
        park = row["Branch"]
        location = row["Reviewer_Location"
        totals[park][location][0] += row["Rating"]
        totals[park][location][1] += 1

     resul ={}
     for park,locations in totls.iteam(:
         result[park] = {
             loc: values[0] / values [1]
             for loc, values in locations.iteams()
         }
         return result
