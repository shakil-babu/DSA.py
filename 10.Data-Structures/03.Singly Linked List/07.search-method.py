def search(self, val):
    if self.head is None:
        print("Linked list empty!")
    else:
        current = self.head
        while current is not None:
            if current.val == val:
                return True
            current = current.next
        return False
