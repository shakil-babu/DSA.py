def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    if llist is None:
        llist = node
    else:
        cur = llist
        node.next = cur
        llist = node

    return llist
