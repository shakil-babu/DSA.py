def addToBegin(self, val):
    node = Node(val)
    if self.head is None:
        self.head = node
        self.tail = self.head
    else:
        self.head.prev = node
        node.next = self.head
        self.head = node
    self.length += 1
