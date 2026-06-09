Music Playlist Manager
A CLI app to manage a personal music library — add songs, build playlists, search by metadata, and export reports. Built to exercise six core Python concepts in a single cohesive project.

Project requirements

Load and persist the library using data/library.json via json.load and json.dump with a Song dataclass
Parse and validate song metadata with regular expressions — duration format 3:45, genre allowlist, partial title search
Wrap library functions with decorators: @log_action for audit logging, @validate_song for input checking
Sort and filter the library using lambdas — sort by title, duration, or BPM; filter by genre
Build a custom PlaylistIterator class supporting normal, shuffle, and loop playback modes via __iter__ and __next__
Manage session state with variable scope — module-level SESSION_STATS dict; understand local vs global vs module scope
Organise code across multiple modules: library.py, playlist.py, search.py, decorators.py, main.py


Features to build

Add & remove songs — persist changes to JSON on every action
Search & filter — regex title search, genre filter, sort by any field
Playlist playback — iterate a playlist in order, shuffle, or loop
Export report — write a playlist summary to a .txt or .md file
Session stats — show songs played and actions taken this session


File structure
music_manager/
├── main.py            # CLI entry point and menu loop
├── library.py         # Song dataclass, add/remove, JSON I/O
├── playlist.py        # PlaylistIterator, playlist management
├── search.py          # Regex parsing, sort/filter with lambdas
├── decorators.py      # @log_action, @validate_song
└── data/
    └── library.json   # Persisted song data (start with empty array [])

Build phases

Phase 1 — Data model & modules
Define a Song dataclass with fields: title, artist, genre, duration (string e.g. "3:45"), bpm (int). Split the project into the five modules from the start. Write load_library, save_library, add_song, remove_song, and list_songs in library.py. Add stub decorators in decorators.py that pass through for now. Wire up a basic CLI menu in main.py.
Concepts: Modules, File I/O, JSON, dataclasses

Phase 2 — Regex parsing & validation
Write parse_duration(s) using regex to convert "3:45" → total seconds. Write validate_genre(s) that checks input against an allowed genre list. Reject bad input with a clear error message. Both functions live in search.py.
Concepts: Regular expressions, input validation

Phase 3 — Decorators
Fill in @log_action to print a timestamped line whenever a song is added, removed, or a playlist is modified. Fill in @validate_song to check the song object before any library function runs.
Concepts: Decorators, higher-order functions

Phase 4 — Sorting with lambdas
Add sort_library(key) to search.py accepting a sort key string ("title", "duration", "bpm") and using a lambda as the key= argument in sorted(). Also use a lambda to filter songs by genre.
Concepts: Lambdas, sorting & filtering

Phase 5 — Custom iterator & playlists
Build PlaylistIterator in playlist.py with __iter__ and __next__. Support three modes: normal (in order), shuffle (random), and loop (restart on StopIteration).
Concepts: Iterators, OOP, random

Phase 6 — Variable scope & CLI polish
Add a module-level SESSION_STATS dict that tracks songs played and actions taken this session. Practice using global deliberately. Wire everything into a clean, complete CLI menu in main.py.
Concepts: Variable scope (local vs global vs module-level), CLI

Stretch goals

Export to markdown — generate a formatted .md file of a playlist
Genre stats — use collections.Counter for a breakdown of songs and total playtime per genre
Fuzzy search — extend search with regex partial matching, case-insensitive
Rich CLI — install the rich library and display the library as a formatted table with colour-coded genres


Technologies

Python 3.10+
Standard library only: dataclasses, json, re, random


Progress tracker

 Phase 1 — Data model & modules
 Phase 2 — Regex parsing & validation
 Phase 3 — Decorators
 Phase 4 — Sorting with lambdas
 Phase 5 — Custom iterator & playlists
 Phase 6 — Variable scope & CLI polish