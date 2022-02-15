def deleteFromBegin(self):
    if self.head is None:
        print("Linked list is emty!")

    else:
        deleteNode = self.head
        self.head = deleteNode.next
        self.length -= 1

        if self.length == 0:
            self.tail = None
