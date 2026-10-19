# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
    # the function counts all the capital letters as well as all the underscore letters in a string
# - what is the input data and type
    # the input data is the one hardcoded into the print lines below the function, the input type is a string
# - what is the return value and type
    # the return value is both the count for upper and lowercase letters, both integers


# function implementation

def mystery_func(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
    # upper being 0, lower being 3.
    # upper being 2, lower being 13
    # upper being 0, lower being 0
    # upper being 3, lower being 0
# Uncomment the lines of code one by one and run the program
# to see if you are right?

# print(mystery_func("X"))
# print(mystery_func("[2, 3]"))
print("list:", mystery_func("[2, 3]"))
