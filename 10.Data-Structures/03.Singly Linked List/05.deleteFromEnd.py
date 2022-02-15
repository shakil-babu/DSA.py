def deleteFromEnd(self):
    if self.head is None:
        print("Linked list is emty!")

    elif self.head.next is None:
        self.head = None
    else:
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.length -= 1


"""
def deleteFromEnd(self):
        if self.head is None:
            print("Linked list is emty!")
        else:
            current = self.head
            newTail = current
            while current.next is not None:
                newTail = current
                current = current.next
            newTail.next = None
            self.length -= 1

"""
