def addAfterNode(self, val, newVal):
    node = Node(newVal)
    if self.head is None:
        self.head = node
        node.next = self.head
    else:
        current = self.head
        while current.next != self.head:
            if current.val == val:
                break
            current = current.next

        if current.next == self.head:
            current.next = node
            node.next = self.head
        else:
            node.next = current.next
            current.next = node
