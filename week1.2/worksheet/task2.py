# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

def read_numbers():
    line = input("Enter some numbers, separated by spaces:")
    numbers = [float(item) for item in line.split()]
    return numbers

numbers = read_numbers()
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()

minimum = min(numbers)
print("Minimum =", minimum)

maximum = max(numbers)
print("Maximum =", maximum)

sum = sum(numbers)
length = len(numbers)
mean = sum / length
print("Mean =", mean)

median_index = length // 2
if length % 2 == 1:
    median = numbers[median_index]
else:
    median = (numbers[median_index - 1] + numbers[median_index]) / 2
print("Median =", median)



