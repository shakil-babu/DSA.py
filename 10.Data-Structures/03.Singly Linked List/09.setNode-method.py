def setNode(self, val, newValue):
    if self.head is None:
        print("Linked list is empty!")
    else:
        current = self.head
        while current is not None:
            if current.val == val:
                current.val = newValue
            current = current.next

        return "Node not found!"
