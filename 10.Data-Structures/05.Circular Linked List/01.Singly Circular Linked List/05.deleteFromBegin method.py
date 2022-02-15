def deleteFromBegin(self):
    if self.head is None:
        print("Linked list is empty!")
        return
    else:
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            self.head = self.head.next
            current.next = self.head
