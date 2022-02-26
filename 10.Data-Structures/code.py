# 10 neat python tricks


# 01. reverse string in python
import itertools
a = 'shakil'
rev = a[::-1]


# 02. transposing a matrix
mat = [[1, 2, 3], [4, 5, 6]]
trans = zip(*mat)
# [(1, 4), (2, 5), (3, 6)]


# 03. store all three values
li = [10, 20, 40]
a, b, c = li


# 04. create a single string
lii = ["i", "am", "shakil"]
print(" ".join(lii))


""" -> 05.
List 1 = ['a', 'b', 'c', 'd']
List 2 = ['p', 'q', 'r', 's']
Write a Python code to print

    ap
    bq
    cr
    ds

"""
li1 = ['a', 'b', 'c', 'd']
li2 = ['p', 'q', 'r', 's']
for x, y in zip(li1, li2):
    print(x, y)


# 06. swap two numbers with one line
a = 10
b = 30
a, b = b, a


# 07. multiply
print("str" * 4)


"""
Trick #8
a = [[1, 2], [3, 4], [5, 6]]
Convert it to a single list without using any loops.
Output:- [1, 2, 3, 4, 5, 6]
"""

a = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a)))


# 09 -> take multiple input
result = map(lambda x: int(x), raw_input().split())
