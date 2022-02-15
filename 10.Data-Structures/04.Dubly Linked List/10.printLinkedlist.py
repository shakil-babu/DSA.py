def print(self):
    if self.head is None:
        print("DLL is empty!")
    else:
        current = self.head
        print("Null --> ", end='')
        while current is not None:
            print(current.val, end="--> ")
            current = current.next
        print("Null")
