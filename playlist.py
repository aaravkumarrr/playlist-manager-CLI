import library
import search
import questionary
import datetime
import random
import decorators


def __iter__(self):
    self.a = 1
    return self

def __next__(self):
    x = self.a
    self.a += 1
    return x

def PlaylistIterator():
    decision = questionary.select("How would you like to play the songs?", choices = ["In Order","Shuffle","Loop", "Quit"]).ask()

    if decision == "In Order":
        songs = library.load_library()
        song_iterator = iter(songs)
        exit = False
        while not exit:
            decision = questionary.select("", choices = ["Next Song","Quit"]).ask()
            if decision == "Next Song" :
                try:
                    current = next(song_iterator)
                    print("Now Playing: ", current.title, " by ", current.artist)
                except StopIteration:
                    print("Playlist has ended.")
                    exit = True
            else:
                exit = True
    elif decision == "Shuffle":
        songs = library.load_library()
        random.shuffle(songs)
        song_iterator = iter(songs)
        exit = False
        while not exit:
            decision = questionary.select("", choices = ["Next Song","Quit"]).ask()
            if decision == "Next Song" :
                try:
                    current = next(song_iterator)
                    print("Now Playing: ", current.title, " by ", current.artist)
                except StopIteration:
                    print("Playlist has ended.")
                    exit = True
            else:
                exit = True
    elif decision == "Loop":
        songs = library.load_library()
        song_iterator = iter(songs)
        exit = False
        while not exit:
            decision = questionary.select("", choices = ["Next Song","Quit"]).ask()
            if decision == "Next Song" :
                try:
                    current = next(song_iterator)
                    print("Now Playing: ", current.title, " by ", current.artist)
                except StopIteration:
                    song_iterator = iter(songs)
            else:
                exit = True
    


