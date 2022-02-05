def solve(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            print(i, j)


"""
O(n) operation inside of an O(n) operation. so the time complexity -

-> O(n * n)
-> O(n^2)
  
TIme complexity = O(n^2)
space complexity = O(1)

"""


def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item)


quadratic_algo([4, 5, 6, 8])
