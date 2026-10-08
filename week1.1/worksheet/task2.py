"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: James Malone
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
try:
        save_month = int(input("How much do you wish to save each month?"))
        total_year = save_month * 12
        print(f"You will save £{total_year} every year.")
        total_year_interest = total_year * 1.008
        print(f"With interest, you will save £{total_year_interest:.2f} per year.")
except ValueError:
        print("Invalid amount")



