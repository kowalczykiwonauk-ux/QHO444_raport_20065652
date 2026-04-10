"""TEXT USER INTERFACES (TUI). This module handles all communication between the program and the user.
 Its functions are responsible for displaying information and collecting user input as needed.
 Each function should make use of its parameters to manage input and output operations, and may return structured data
  such as lists or tuples where appropriate."""
from fontTools.feaLib import location

MAIN_MENU_OPTIONS = ["A", "B", "C", "X"]
VIEW_MENU_OPTIONS = ["A", "B", "C", "D","X"]
VISUAL_MENU_OPTIONS = ["A", "B", "C", "X"]
EXIT_MENU_OPTIONS = ["TXT", "CVS", "JSON"]

def  disply_title():
    """Display the title of the TUI."""
    print("=" * 60)
    print("     Disneyland Reviews Analysis system")
    print("=" * 60)


def display_loaded(row_count):
    "confirmation that data has been loaded and display the row count"
    print(f"\nData loaded successfully! {row_count} records found.\n")

def display_main_menu():
    """Display the View Data sub-menu and return the user's validated choice."""
    print("\nPlease enter one of the following options:")
    print("A -> View reviews for a Park")
    print("B -> Show number of reviews by Location")
    print("C -> Show average rating for a Park in a Year")
    print("D -> Show average  score per Park by reviewer location")
    print("X -> Return to MAIN MENU")
    return_get_choice("Your choice:", VIEW_MENU_OPTIONS)

def display_visual_menu():
    """Display the Visualise Data sub-menu and return the user's validated choice."""
    print("\nPlease enter one of the following options:")
    print("A -> Most reviews Park")
    print("B -> Park ranking by Nationality")
    print("C -> Most popular month  by Park")
    print("X -> Return to MAIN MENU")
    return_get_choice("Your choice: ", VISUAL_MENU_OPTIONS)

def confirm_choice(choice):
    """Ask the user to select a park fro a numbered list and return the park name:"""
    print("\nAvailable parks:")
    for i, park in enumerate(prks, 1):
        print(f" {i}. {park}")
    while True:
        entry =input("Enter park number:").strip()
        if entry.isdigit():
            inde = int(entry) - 1
            if 0< = index < len(parks):
                return  parks[index]
        print(f"Invalid input. Please enter a number between 1 and {len(paks)}.")

def get_location():
    """Ask the user to enter a reviewer location and return the stripped string."""
    while True:
        location = input("enter reviewer location:").strip()
        if location:
            return location
        print("Location cannot be empty. Please try again.")

def get_year()
    """Ask the user to enter  a year and return it as an integer """
    while True:
        year = input("enter year (e.g. 2026:").strip()
        if year.isdigit() and len(year) == 4:
            return int(year)
        print("Invalid year. Please enter a 4 digit year.")

def get_export_format():
    """Ask the user to select an export format and return the choice."""
    print("\nSelect export format:")
    for i, fmt in enumerate(EXPORT_FORMATS, 1):
        print(f" {i}. {fmt}")
    while True:
        entry = input("Enter export format:").strip()
        if entry.isdigit():
            index =int(entry) - 1
            if 0< = index < len(EXPORT_FORMATS):
                return EXPORT_FORMATS[index]
        print(f"Invalid input. Please enter 1, 2, or 3.")

def display_review(park, reviews):
    """DDisplay all reviews for a given park."""
    print(f"\n --- Reviews for {park} ({len(reviews)} total) --:")
    if not reviews:
        print("No reviews found.")
        return
    print(f{'ID':<12} {'Rating' :<8}{'Year-Month' :<12} {'Location'}")
    print("-"*60)
    for reviews in reviews:
        print(
            f"{review['Review_ID']:<12} {review['Rating']:<8} "
            f"{review['Year_Month']:<12}  {review['Reviewr_Location]}"
        )
        
def display_review_count(park, location, reviews):
    """Display the number of reviews  fro a park from a location"""
    print(f"\n{park} has received {count} review(s) from {location}")

def display_average_rating(park,year, average):
    """Display the average rating for a park  in a given year"""
    if average is None:
        print(f"\No reviews found for {park} in {year}.")
    else:
        print(f"\Average rating for {park} in {year}: {average:.2f} / 5.00")

def display_avg_by_location(results):
    """Display the average score per park for every reviewer loaction"""
    for park, location_data in sorted(results.items()):
        print(f"\n{'=' * 50})
        print(f"   {park}")
        print(f"{'=' * 50}")
        print(f"  {'Location':<40} {'Avg Rating'}")
        print(f"  {'-'* 50}")
        for location, avg in sorted(location_data.items(), key=lambda x: -x[1]):
            print(f"  {location:<40} { ava:.2f}")

def display_export_success(filepath):
    """Confirm that data has been exported successfully"""
    print(f"\nData exported succesully.")

def display_invalid_choice():
    """Inform the user that their menu input was invalid"""
    print("Invalid choice. Please one of the listed options.")

def dispaly_exit():
    """Display a goodbye message when the user exits."""
    print(2\nThnak you for using the Disneyland Reviews analysis system. Goodbye!")

#------------------------------------
#