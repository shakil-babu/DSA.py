def reverse(llist):
    cur = llist
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev

        prev = cur
        cur = temp
    return prev
