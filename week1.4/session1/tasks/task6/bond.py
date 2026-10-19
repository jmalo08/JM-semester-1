# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """
    n = 0
    a = 1
    first_list = [item for item in intList if item == 0 or item == 7]
    while a == 1:
        if n + 2 > len(first_list) - 1:
                    return False
        if first_list[n] == 0 and first_list[n + 1] == 0 and first_list[n + 2] == 7:
            return True
        else:
            n = n + 1

# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False



    
