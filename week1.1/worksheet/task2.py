"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: James Malone
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
save_month = int(input("How much do you wish to save each month?"))

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
total_year = save_month * 12
print("The total money you will have saved by the end of the year, excluding interest, is £", total_year)

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
total_year_interest = total_year + (total_year * 1.08)
print("The total money you wil have saved by the end of the year, including interest, is £", total_year_interest)



