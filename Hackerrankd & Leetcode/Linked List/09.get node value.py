def getNode(llist, positionFromTail):
    a, b = llist, llist
    for i in range(positionFromTail):
        a = a.next

    while a.next:
        a = a.next
        b = b.next

    return b.data
