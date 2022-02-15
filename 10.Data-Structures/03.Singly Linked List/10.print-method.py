def Print(self):
    if self.head is None:
        print("Linked list is emty!")
    else:
        current = self.head
        while current is not None:
            print(current.val, "--->", end=" ")
            current = current.next
        print("Null")
