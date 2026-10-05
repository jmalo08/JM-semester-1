# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# tomato
both = fruit.intersection(vegetables)
print(both)
# Why does the following code diplay five items?
# when combining the two tuples, there are 5 instances of a fruit / vegetable. even tough there are 6 elements overall, tomato is repeated. 

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("pineapple")
print(fruit)
# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)
# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables))
