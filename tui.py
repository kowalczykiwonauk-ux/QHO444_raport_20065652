"""TEXT USER INTERFACES (TUI). This module handles all communication between the program and the user.
 Its functions are responsible for displaying information and collecting user input as needed.
 Each function should make use of its parameters to manage input and output operations, and may return structured data
  such as lists or tuples where appropriate."""

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
                return EXPORT_FORMATS
