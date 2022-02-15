def addToEnd(self, val):
    node = Node(val)
    if self.head is None:
        self.head = node
        node.next = self.head
        return
    else:
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = node
        node.next = self.head
