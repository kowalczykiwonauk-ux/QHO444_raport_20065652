"""These modules visualize the dat - any visualisation  is generated via functions"""

import matplotlib.pyplot as plt

MONTH_NAMES = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]

def show_reviews_per_park_pie(review_counts):
    """ Display the reviews per park pie
    ----------
    Parameters
    -----------
    review_counts: dict
    {park_name: count} mapping returned by process.get_review_counts_per_park().
    """
    parks = list(review_counts.keys())
    counts = [review_counts[p] for p in parks]

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        counts,
        labels=parks,
        autopct="%1.1f%%",
        startangle=140,
    )
    for autotext in autotexts:
        autotext.set_fontsize(9)

    ax.set_title("Number of Reviews per Disneyland Park", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

def show_top_locations_bar(park, location_averages):
    """
    Display a bar chart of the top 10 locations with the highest average rating
    for the specified park.

    ----------
    Parameters
    ----------
    park : str
        Name of the park.
    location_averages : list[tuple]
        [(location, avg_rating), ...] sorted descending, max 10 items.
    """
    if not location_averages:
        print(f"No data available for {park}.")
        return

    locations = [item[0] for item in location_averages]
    averages = [item[1] for item in location_averages]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(locations, averages, color="steelblue", edgecolor="white")

    ax.set_title(
        f"Top 10 Locations by Average Rating — {park}",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel("Reviewer Location", fontsize=12)
    ax.set_ylabel("Average Rating (out of 5)", fontsize=12)
    ax.set_ylim(0, 5.5)
    ax.tick_params(axis="x", rotation=35)


    for bar, avg in zip(bars, averages):
        ax.text(
             bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.05,
            f"{avg:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
    )

    plt.tight_layout()
    plt.show()

def show_avg_rating_by_month_bar(park, month_data):
    """
    Display a bar chart showing the average rating per month of the year for a park.

    ----------
    Parameters
    ----------
    park : str
        Name of the park.
    month_data : list[tuple]
        [(month_number, avg_rating), ...] sorted by month number.
    """
    if not month_data:
        print(f"No data available for {park}.")
        return

    month_numbers = [item[0] for item in month_data]
    averages = [item[1] for item in month_data]
    labels = [MONTH_NAMES[m - 1] for m in month_numbers]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(labels, averages, color="coral", edgecolor="white")

    ax.set_title(
        f"Average Rating by Month — {park}",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Average Rating (out of 5)", fontsize=12)
    ax.set_ylim(0, 5.5)

    for bar, avg in zip(bars, averages):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            f"{avg:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.show()


