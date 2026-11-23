import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

number = int(input("Choose your number"))
new_list = random.sample(names, k=number)
# Display the chosen names, one per line
for name in new_list:
    print(name)
