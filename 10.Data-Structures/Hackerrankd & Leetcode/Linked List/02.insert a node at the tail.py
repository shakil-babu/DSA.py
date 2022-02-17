def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head is None:
        head = node
    else:
        cur = head
        while cur.next:
            cur = cur.next

        cur.next = node
        node.next = None
    return head
