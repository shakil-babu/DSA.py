"""
write a function that calculates the sum of all numbers 
from 1 up to (and including) some number n.
"""


def addUpTo(n):
    total = 0
    for i in range(n):
        total += i

    return total


"""

in above code:

    n additions

    n assignments

    n additions and n assignments

    1 assignment

    1 assignment

    n comparisons


Number of operations is (eventually) bounded by a multiple of n(say, 10n)
time complexity -> O(n)


*/

/*

TIme complexity = O(n)
space complexity = O(1)


"""


def linearSearch(arr, target):
    for item in arr:
        if item == target:
            return 1

    return -1


"""
Time comlexity : O(n)
"""


def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])

"""
Time comlexity : O(n)
"""


def linear_algo(items):
    for item in items:
        print(item)

    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])

# In the script above, there are two for-loops that iterate over the input items list.
# Therefore the complexity of the algorithm becomes O(2n), however in case of infinite
# items in the input list, the twice of infinity is still equal to infinity,
# therefore we can ignore the constant 2 (since it is ultimately insignificant)
# and the complexity of the algorithm remains O(n).
