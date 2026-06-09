from dataclasses import dataclass
import json
import os
import search
import decorators

script_dir = os.path.dirname(os.path.abspath(__file__))
datalibrary_path = os.path.join(script_dir, "data-library.json")

@dataclass
class Song:
    title: str
    artist: str
    genre: str
    duration: str
    bpm: int

def load_library():
    try:
        with open(datalibrary_path,"r") as library:
            songlib = json.load(library)
    except FileNotFoundError:
        songlib = []
    except json.JSONDecodeError:
        songlib = []
    return songlib

def save_library(new_library):
    with open(datalibrary_path, "w") as lib:
        json.dump(new_library, lib)

@decorators.log_action
def add_song():

    valid_entry = [0,0,0,0,0]
    passed = False

    while not passed:
        # Title validity
        while valid_entry[0] == 0:
            song_title = input("Please enter the song title\n")
            if len(song_title)<80:
                if song_title.strip():
                    valid_entry[0] = 1
                else:
                    print("Your entry must contain characters")
            else:
                print("Your entry has too many characters")
        # Artist name validity
        while valid_entry[1] == 0:
            artist = input("Please enter the artist name\n")
            if len(artist)<80:
                if artist.strip():
                    valid_entry[1] = 1
                else:
                    print("Your entry must contain characters")
            else:
                print("Your entry is too long")
        
        # genre validity
        while valid_entry[2] == 0:
            genre = input("Please enter the genre\n")
            if search.validate_genre(genre):
                valid_entry[2] = 1
            
        # duration validity
        while valid_entry[3] == 0:
            duration = input("Please enter the duration\n")
            if search.parse_duration_dur_as_input(duration) < 900:
                valid_entry[3] = 1
            else: 
                print("Your entry is too long.")

        # broken, needs to be fixed.
        while valid_entry[4] == 0:
            bpm = int(input("Please enter the bpm\n"))
            
            if bpm > 0:
                valid_entry[4] = 1
            else:
                print("bpm cannot be negative")
        
        passed = all(x == 1 for x in valid_entry)



    songlibrary = load_library()
    songlibrary.append({"title":song_title, "artist": artist, "genre": genre, "duration": duration, "bpm": bpm})
    with open(datalibrary_path,"w") as library:
        json.dump(songlibrary, library)
    
@decorators.log_action
def remove_song():
    song_to_remove = input("Which song would you like to remove?")
    songs = load_library()
    for item in songs:
        if item["title"] == song_to_remove:
            songname = item["title"]
            songs.remove(item)
            print(songname, " has been removed from your playlist.")
        else:
            print("That song is not in your library.")
    save_library(songs)

@decorators.log_action
def list_songs():
    songs = load_library()
    print("-----------------------------------------------+--------------------------------+-------------------------------+------------------------+---------------")
    print(f"Title                                          |Artist                          |Genre                          |Duration                |BPM            ")
    print("-----------------------------------------------+--------------------------------+-------------------------------+------------------------+---------------")   
    for item in songs:
        print(f"{item["title"]:<47}|{item["artist"]:<32}|{item["genre"]:<31}|{item["duration"]:<24}|{item["bpm"]:<16}")
