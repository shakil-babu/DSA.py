def deleteFromEnd(self):
    if self.head is None:
        print("Linked list is empty!")
        return
    else:
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            prev = current
            while current.next.next != self.head:
                current = current.next

            current.next = self.head
