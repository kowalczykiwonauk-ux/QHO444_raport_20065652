# Module Code: 	QHO444 Software artifact with report

#This module manages the overall flow of the program.
#It directs how the user engages with the system and determines the program’s behaviour.
# It relies on the other modules to handle user interaction, perform processing tasks, and present information visually.


#Notes: model 'tui' should store user input/output
 #      model 'process' is used for any action taken
 #      model 'visual' will represent any visualization done

import os
import process
import tui
import visual

DATA_PATH = os.path.join("data", "disneyland_reviews.csv")

#---------------------------------------------------------------------
#Sub -menu handlers
#--------------------------------------------------------------------

def handle_view_data(dataset, parks) :
    """ Handle the 'view data' sub-menu ( main menu option A)."""
    while True:
        choice = tui.display_view_menu()
        tui. confirm_choice(choice)

        if choice == "A" :
            park =tui.get_park(parks)
            reviews = process.get_review_for_park(dataset, park)
            tui.display_reviews(park,reviews)

        elif choice == "B" :
            park =tui.get_park(parks)
            location = tui.get_location()
            count = process.get_review_count_by_location(dataset, park, location)
            tui.dispplay_review_count(park, location, count)

        elif choice == "C" :
            park =tui.get_park(parks)
            year = tui.get_year()
            average = process.get_average_review(dataset, park, year)
            tui.display_average_rating(park, year, average)

        elif choice == "D" :
            results = process.get_average_rating_per_location_per_park(dataset)
            tui.display_avg_by_location(results)

        elif choice == "X":
            break

def handle_visualise_data(database, parks):
    """Handle the 'Visualise Data' sub-menu  (main menu ption B)"""
    while True:
        choice: tui.dispplay_visula-menu()
        tui. confirm_choice(choice)

        if choice == "A" :
            counts =process.get_review_counts_per_park (database)
            visual.show_reviews_per_park_pie(counts)

        elif choice == "B":
            park = tui.get_park(parks)
            top_locations = process.get_top_loctions_by_avg_rating(dataset,park)
            visual.show_top_locations_bar(park, top_locations)

        elif choice == "C":
            park =tui.get_park(parks)
            month_data =process.get_avg_rating_by_month(dataset, park)
            visual.show_avg_by_month_bar(park,month_data)

        elif choice == "X" :
            break
def handle_export_data(dataset):
    """Handle the 'Export Data' future using OOP (main menu option C)"""
    fmt = tui.get-export_format()
    summary = process.get_park_summary(dataset)
    ext =exporter.create_exporter(fmt, summary)
    filepath = exp.export()
    tui.display_export_success(filepath)

#------------------------------------------------------------
#MAIN ENTRY POINT
#----------------------------------------------------

def main():
    """Run the Disneyland Reviews analysis System."""
    tui.display_title()

    #Load data once at startup
    dataset = process.load_data(DATA_PATH)
    tui.display_loaded(len(dataset))

    parks =process.get_unique_parks(dataset)

#Main application loop
while True:#
    choice = tui.display_main_menu()
    tui. confirm_choice(choice)

    if choice =="A" :
        handle_view_data(dataset, parks)

    elif choice =="B" :
        handle_visualise_data(dataset, parks)

    elif choice =="C" :
        handle_visualise_data(dataset)

    elif choice =="X" :
        tui.display_exit()
        break

if__name__ == "__main__"
main()




