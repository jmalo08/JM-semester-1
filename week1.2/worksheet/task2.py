# Worksheet 1.2: Task 2 Solution
from util import read_numbers

def read_numbers():
    line = input("Enter some numbers, separated by spaces:")
    numbers = [float(item) for item in line.split()]
    return numbers

numbers = read_numbers()
numbers.sort()
minimum = numbers.pop(0)
print(minimum)
maximum = numbers.pop()
print(maximum)
sum = sum(numbers)
length = len(numbers)
mean = sum / length
print(mean)
median_index = length / 2




