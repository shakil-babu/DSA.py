def enqueue(self, item):
    node = Node(item)
    if self.head is None:
        self.head = node
        self.tail = node
    else:
        node.next = node
        self.head = node
    self.length += 1
