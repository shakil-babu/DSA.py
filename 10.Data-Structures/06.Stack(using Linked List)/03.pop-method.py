def pop(self):
    if self.head is None:
        print("stack is empty!")
        return
    if self.length == 1:
        self.head = None
        self.tail = None
        self.length -= 1
    else:
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.length -= 1
        return current.val
