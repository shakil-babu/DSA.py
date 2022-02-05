
# The Average Case times listed for dict objects assume that the hash function for the objects is
# sufficiently robust to make collisions uncommon. The Average Case assumes the keys used
# in parameters are selected uniformly at random from the set of all keys.

# Note that there is a fast-path for dicts that (in practice) only deal with str keys
# this doesn't affect the algorithmic complexity, but it can significantly affect the
# constant factors: how quickly a typical program finishes.


"""
k in d
O(n)

Copy[3]
O(n)

Get Item
O(n)

Set Item[1]
O(n)

Delete Item
O(n)

Iteration[3]
O(n)

"""
