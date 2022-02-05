# sum
def sum(a, b):
    sum = a+b
    return sum


"""
write a function that calculates the sum of all numbers 
from 1 up to (and including) some number n.
"""


def addUpTo(n):
    return (n * (n + 1)) / 2


"""
/*

in above code - 
              1 multipication
              1 addition
              1 division

              3 simple operation, regardless of the size of n

Always 3 operations
O(1)

=================
TIme complexity = O(1);
space complexity = O(1);

"""


def constant_algo(items):
    result = items[0] * items[0]
    print()


constant_algo([4, 5, 6, 8])
