# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
music = {"Pink Floyd": ["The Dark Side of the Moon", "The Wall", "Wish you were here", "The Division Bell", "Animals", "Echoes"]}
# (keys are artist names, values are lists of album names)

# Pretty-print the data structure
pprint(music)
# Display details of one album recorded by a specific artist
music.get("Pink Floyd")