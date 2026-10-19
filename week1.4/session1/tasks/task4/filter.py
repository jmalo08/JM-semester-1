# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def read_numbers():
    line = input("Enter some numbers, separated by spaces:")
    numbers = [int(item) for item in line.split()]
    return numbers

numbers = read_numbers()

def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0]

print("The positive numbers are",filter_positive_numbers(numbers))
