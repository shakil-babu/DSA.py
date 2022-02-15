def deleteAnyNodeByValue(self, val):
    if self.head is None:
        print("Linked list is emty!")

    elif self.head.val == val:
        self.head = self.head.next
        self.length -= 1
    else:
        current = self.head
        while current.next is not None:
            if current.next.val == val:
                break
            current = current.next

        if current.next is None:
            print("Node is not present!")

        else:
            current.next = current.next.next
            self.length -= 1
