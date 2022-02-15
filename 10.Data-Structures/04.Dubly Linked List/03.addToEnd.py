def addToEnd(self, val):
    node = Node(val)
    if self.head is None:
        self.head = node
        self.tail = self.head
    else:
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    self.length += 1
