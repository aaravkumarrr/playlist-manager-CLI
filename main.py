import library
import questionary
from questionary import Choice
import search
import playlist

def menu():
    decision = questionary.select("Which action would you like to perform?", choices = ["Add Song", "Remove Song", "List Songs", "Play songs", "Exit"]).ask()
    
    if decision == "Add Song":
        library.add_song()
    elif decision == "Remove Song":
        library.remove_song()
    elif decision == "List Songs":
        library.list_songs()
        decision = questionary.select("Would you like to sort by a category?", choices=["Yes", "No"]).ask()
        if decision == "Yes":
            search.sort_library()
        # COMPLETE ABOVE LOOP
    elif decision == "Play songs":
        playlist.PlaylistIterator()
    elif decision == "Exit":
        print("TBD")
        

def main():
    while True:
        menu()


if __name__ == "__main__":
    main()