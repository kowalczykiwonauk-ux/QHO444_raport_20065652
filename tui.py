"""TEXT USER INTERFACES (TUI). This module handles all communication between the program and the user.
 Its functions are responsible for displaying information and collecting user input as needed.
 Each function should make use of its parameters to manage input and output operations, and may return structured data
  such as lists or tuples where appropriate."""

MAIN_MENU_OPTIONS = ["A", "B", "C", "X"]
VIEW_MENU_OPTIONS = ["A", "B", "C", "D", "X"]
VISUAL_MENU_OPTIONS = ["A", "B", "C", "X"]
EXPORT_FORMATS = ["TXT", "CSV", "JSON"]


def display_title():
    """Display the application title."""
    print("=" * 60)
    print("       Disneyland Reviews Analysis System")
    print("=" * 60)


def display_loaded(row_count):
    """Confirm data has been loaded and display the row count."""
    print(f"\nData loaded successfully! {row_count} records found.\n")


def display_main_menu():
    """Display the main menu and return the user's validated choice."""
    print("\nPlease enter one of the following options:")
    print("  A - View Data")
    print("  B - Visualise Data")
    print("  C - Export Data")
    print("  X - Exit")
    return _get_choice("Your choice: ", MAIN_MENU_OPTIONS)


def display_view_menu():
    """Display the View Data sub-menu and return the user's validated choice."""
    print("\nPlease enter one of the following options:")
    print("  A - View Reviews for a Park")
    print("  B - Number of Reviews by Location")
    print("  C - Average Rating for a Park in a Year")
    print("  D - Average Score per Park by Reviewer Location")
    print("  X - Return to Main Menu")
    return _get_choice("Your choice: ", VIEW_MENU_OPTIONS)


def display_visual_menu():
    """Display the Visualise Data sub-menu and return the user's validated choice."""
    print("\nPlease enter one of the following options:")
    print("  A - Most Reviewed Parks")
    print("  B - Park Ranking by Nationality")
    print("  C - Most Popular Month by Park")
    print("  X - Return to Main Menu")
    return _get_choice("Your choice: ", VISUAL_MENU_OPTIONS)


def confirm_choice(choice):
    """Confirm the user's menu selection."""
    print(f"\nYou selected: {choice}")


def get_park(parks):
    """Ask the user to select a park from a numbered list and return the park name."""
    print("\nAvailable parks:")
    for i, park in enumerate(parks, 1):
        print(f"  {i}. {park}")
    while True:
        entry = input("Enter park number: ").strip()
        if entry.isdigit():
            index = int(entry) - 1
            if 0 <= index < len(parks):
                return parks[index]
        print(f"Invalid input. Please enter a number between 1 and {len(parks)}.")


def get_location():
    """Ask the user to enter a reviewer location and return the stripped string."""
    while True:
        location = input("Enter reviewer location: ").strip()
        if location:
            return location
        print("Location cannot be empty. Please try again.")


def get_year():
    """Ask the user to enter a year and return it as an integer."""
    while True:
        year = input("Enter year (e.g. 2018): ").strip()
        if year.isdigit() and len(year) == 4:
            return int(year)
        print("Invalid year. Please enter a 4-digit year.")


def get_export_format():
    """Ask the user to select an export format and return the choice."""
    print("\nSelect export format:")
    for i, fmt in enumerate(EXPORT_FORMATS, 1):
        print(f"  {i}. {fmt}")
    while True:
        entry = input("Enter format number: ").strip()
        if entry.isdigit():
            index = int(entry) - 1
            if 0 <= index < len(EXPORT_FORMATS):
                return EXPORT_FORMATS[index]
        print(f"Invalid input. Please enter 1, 2, or 3.")


def display_reviews(park, reviews):
    """Display all reviews for a given park."""
    print(f"\n--- Reviews for {park} ({len(reviews)} total) ---")
    if not reviews:
        print("No reviews found.")
        return
    print(f"{'ID':<12} {'Rating':<8} {'Year-Month':<12} {'Location'}")
    print("-" * 60)
    for review in reviews:
        print(
            f"{review['Review_ID']:<12} {review['Rating']:<8} "
            f"{review['Year_Month']:<12} {review['Reviewer_Location']}"
        )


def display_review_count(park, location, count):
    """Display the number of reviews for a park from a location."""
    print(f"\n{park} has received {count} review(s) from {location}.")


def display_average_rating(park, year, average):
    """Display the average rating for a park in a given year."""
    if average is None:
        print(f"\nNo reviews found for {park} in {year}.")
    else:
        print(f"\nAverage rating for {park} in {year}: {average:.2f} / 5.00")


def display_avg_by_location(results):
    """Display the average score per park for every reviewer location."""
    for park, location_data in sorted(results.items()):
        print(f"\n{'=' * 50}")
        print(f"  {park}")
        print(f"{'=' * 50}")
        print(f"  {'Location':<40} {'Avg Rating'}")
        print(f"  {'-' * 50}")
        for location, avg in sorted(location_data.items(), key=lambda x: -x[1]):
            print(f"  {location:<40} {avg:.2f}")


def display_export_success(filepath):
    """Confirm that data has been exported successfully."""
    print(f"\nData exported successfully to: {filepath}")


def display_invalid_choice():
    """Inform the user that their menu input was invalid."""
    print("Invalid choice. Please select one of the listed options.")


def display_exit():
    """Display a goodbye message when the user exits."""
    print("\nThank you for using the Disneyland Reviews Analysis System. Goodbye!")


# --------------------
# Internal helper
# --------------------
def _get_choice(prompt, valid_options):
    """Prompt the user until they enter one of the valid options (case-insensitive)."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_options:
            return choice
        display_invalid_choice()
