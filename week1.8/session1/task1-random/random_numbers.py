import random

# Get user to input how many random numbers they want
user_choice = int(input("Enter how many random numbers you want"))
# Generate this many random numbers
random_numbers = random.sample(range(1, 100), k=user_choice)
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as outfile:
    for number in random_numbers:
        outfile.write(f"{number}\n")


