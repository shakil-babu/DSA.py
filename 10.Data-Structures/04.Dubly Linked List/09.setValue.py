def setValue(self, val, newVal):
    if self.head is None:
        print("Dll is empty!")
        return

    current = self.head
    while current is not None:
        if current.val == val:
            current.val = newVal
        current = current.next
