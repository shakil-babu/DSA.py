def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)
    index = 0
    cur = llist
    prev = cur
    while index != position:
        index += 1
        prev = cur
        cur = cur.next

    node.next = prev.next
    prev.next = node
    return llist
