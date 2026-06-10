import re
import questionary
import library

def list_songs_ordered(songs):
    print("-----------------------------------------------+--------------------------------+-------------------------------+------------------------+---------------")
    print(f"Title                                          |Artist                          |Genre                          |Duration                |BPM            ")
    print("-----------------------------------------------+--------------------------------+-------------------------------+------------------------+---------------")   
    for item in songs:
        print(f"{item["title"]:<47}|{item["artist"]:<32}|{item["genre"]:<31}|{item["duration"]:<24}|{item["bpm"]:<16}")

def parse_duration_dur_as_input(duration_string):

    match = re.search(r'[\d+]:',duration_string)
    minutes = match.group()
    match = re.search(r':[\d]+',duration_string)
    seconds = match.group()

    minutes = int(minutes[:-1])
    seconds = int(seconds[1:])

    total_seconds = minutes * 60 + seconds
    return total_seconds

def parse_duration(song):
    duration_string = song["duration"]

    match = re.search(r'[\d+]:',duration_string)
    minutes = match.group()
    match = re.search(r':[\d]+',duration_string)
    seconds = match.group()

    minutes = int(minutes[:-1])
    seconds = int(seconds[1:])

    total_seconds = minutes * 60 + seconds
    return total_seconds
    


def validate_genre(genre):
    valid_genres = ["Pop", "Rock", "Hip-Hop/Rap", "Electronic", "Classical", "Jazz", "R&B/Soul", "Country"]
    if genre not in valid_genres:
        print("This genre is not in the list of valid genres.")
        return False
    else:
        return True
    

    # do this with lambda functions 
def sort_library():
    sortby = questionary.select("What would you like to sort by?", choices = ["title", "duration","bpm","artist", "genre"]).ask()
    songs = library.load_library()
    match sortby:
        case "title":
            decision = questionary.select("Ascending or Descending?", choices=["Ascending","Descending"]).ask()
            if decision == "Ascending":
                songs = sorted(songs, key= lambda song:song.title)
                library.list_songs_given(songs)

            else:
                songs = sorted(songs, key = lambda song: song.title, reverse=True)
                library.list_songs_given(songs)

        case "duration":
            decision = questionary.select("Ascending or Descending?", choices=["Ascending","Descending"]).ask()
            if decision == "Ascending":
                songs = sorted(songs, key = lambda song: parse_duration_dur_as_input(song.duration))
                library.list_songs_given(songs)
            else:
                songs = sorted(songs, key = lambda song: parse_duration_dur_as_input(song.duration), reverse=True)
                library.list_songs_given(songs)
            pass
            

        case "bpm":
            decision = questionary.select("Ascending or Descending?", choices=["Ascending","Descending"]).ask()
            if decision == "Ascending":
                songs = sorted(songs, key= lambda song:song.bpm)
                library.list_songs_given(songs)
            else:
                songs = sorted(songs, key = lambda song: song.bpm, reverse=True)   
                library.list_songs_given(songs)

        case "artist":
            decision = questionary.select("Ascending or Descending?", choices=["Ascending","Descending"]).ask()
            if decision == "Ascending":
                songs = sorted(songs, key= lambda song:song.artist)
                library.list_songs_given(songs)
            else:
                songs = sorted(songs, key = lambda song: song.artist, reverse=True)
                library.list_songs_given(songs)
                
        case "genre":
            decision = questionary.select("Ascending or Descending?", choices=["Ascending","Descending"]).ask()
            if decision == "Ascending":
                songs = sorted(songs, key= lambda song:song.genre)
                library.list_songs_given(songs)
            else:
                songs = sorted(songs, key = lambda song: song.genre, reverse=True)
                library.list_songs_given(songs)