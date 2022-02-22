def deleteNode(llist, position):
    if llist is None:
        return llist

    if position == 0:
        llist = llist.next

    cur = llist
    prev = cur
    index = 0
    while index != position:
        index += 1
        prev = cur
        cur = cur.next
    prev.next = cur.next

    return llist
