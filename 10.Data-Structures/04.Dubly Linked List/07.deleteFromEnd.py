def deleteFromEnd(self):
    if self.head is None:
        print("Dll is empty!")
        return

    if self.head.next is None:
        self.head = None
        self.tail = None

    else:
        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None
