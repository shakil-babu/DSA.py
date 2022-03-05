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
