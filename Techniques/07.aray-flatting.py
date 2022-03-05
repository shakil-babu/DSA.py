"""
Trick #8
a = [[1, 2], [3, 4], [5, 6]]
Convert it to a single list without using any loops.
Output:- [1, 2, 3, 4, 5, 6]
"""

import itertools

a = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a)))
