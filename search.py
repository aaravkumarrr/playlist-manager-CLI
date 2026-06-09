import re

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