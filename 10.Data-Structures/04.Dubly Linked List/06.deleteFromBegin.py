def deleteFromBegin(self):
    if self.head is None:
        print("Dll is empty!")
        return

    if self.head.next is None:
        self.head = None
        self.tail = None

    else:
        current = self.head
        self.head = current.next
        current.prev = None
