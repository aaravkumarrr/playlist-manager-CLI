import library
import questionary
from questionary import Choice


def menu():
    decision = questionary.select("Which action would you like to perform?", choices = ["Add Song", "Remove Song", "List Songs", "Exit"]).ask()
    
    if decision == "Add Song":
        library.add_song()
    elif decision == "Remove Song":
        library.remove_song()
    elif decision == "List Songs":
        library.list_songs()
    elif decision == "Exit":
        print("TBD")
        
        
        

def main():
    while True:
        menu()


if __name__ == "__main__":
    main()