def push(self, item):
    node = Node(item)
    if self.head is None:
        self.head = node
        self.tail = node
    else:
        self.tail.next = node
        self.tail = node
    self.length += 1
