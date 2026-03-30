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
     for park,locations in totls.iteams:
         result[park] = {
             loc: values[0] / values [1]
             for loc, values in locations.iteams()
         }
         return result
    def get_revew_counts_per_park(dataset):
        """Return a dict mapping each ark to its total number of reviews"""
        counts = defaultdict(int)
        for row in dataset:
            counts[row["Branch"]] += 1
        return dict(counts)
    def get_top_coation_by_avg_rating(dataset, park, top_n=10):
        """
        For a given park, return thr top_n locations with the highest average rating.
        Returns a list of (location, average_rating) tuples, sorted descending.
       """
        park_data =defaultdict(lambada: [0, 0 ])
        for row in dataset:
            if row["Branch"] == park:
                lock =row["Reviewer_Location"]
                park_data[loc][0] +=row["Rating"]
                park_data[loc][1] += 1

        averages = [
            (loc, values [0] / values [1])
            for loc, vlues in park_data.items()
            ]
        averages.sort(key=lambda x: -x[1])
        return averages[:top_n]

    def get_avg_rating_by_month(dataset, park):
        """For a given park, return a list of(month_number, average_rating) tuples
        ordered by calendar month (12). Months with no review are omitted
        """
        month_totals = defaltdict(lambda:[0,0])
        for row in dataset:
            if row["Branch"] == park:
                parts =row["Year_Month"].split("-")
                if len(parts) <2 or not parts[1].isigit():
                    continue
                    monh = int(parts[1])
                    month_totals[month][0] += row["Rating"]
                    month_totals[month][1] += 1

        return sorted(
            [(month,value [0] / values [1]) for month, values in month_totals.items()],
            key=lambda x: x[0]
        )

    def get-park_summary(dataset):
    """Return a dict mapping each park to summary dict containing:
    - num_reviews  (int)
    - num_positive (int) ratings >= 4 count as positive
    -avg_rating  (float
    -num_countries (int) district Reviewer_Location values
    """

    accumulator =defaultdict(
        lambda: {"ratings": [], "locations": set ()}
    )
    for row in datase:
        park= row ["Branch"]
        accumulator[park]["ratings"].append(row)["Ratings"])
        accumulator[park]["locations"].add(row["Reviewer_Location"])


    summary ={}
    for park, data in accumulator.items():
        ratings = data["rattings"]
        summary[park]={
        "num_reviews": len(ratings),
        "num_possitive": sum(1 for r in ratings if r>4),
        "avg_rating": raound(sum(ratings) / len(atings) ,2),
        "num_countries": len(data["locations"]),
        }
    return summary
