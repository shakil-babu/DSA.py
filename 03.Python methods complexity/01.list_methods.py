"""
The Average Case assumes parameters generated uniformly at random.
Internally, a list is represented as an array; the largest costs come from growing
 beyond the current allocation size (because everything must move), or from inserting 
 or deleting somewhere near the beginning (because everything after that must move).
 If you need to add/remove at both ends, consider using a collections.deque instead. 


Operation :
------------------------

Copy
O(n)

Append[1]
O(1)

Pop last
O(1)

Pop intermediate[2]
O(n)

Insert
O(n)

Get Item	
O(1)

Set Item	
O(1)

Delete Item	
O(n)

Iteration	
O(n)

Get Slice	
O(n)

Del Slice
O(n)

Set Slice
O(k+n)

Extend[1]
O(n)

Sort
O(n log n)

"""
