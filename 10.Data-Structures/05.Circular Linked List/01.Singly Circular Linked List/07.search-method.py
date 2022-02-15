def search(self, value):
    position = 0
    found = 0
    if self.head is None:
        print("The linked list does not exist")
    else:
        current = self.head
        while current:
            position = position + 1
            if current.val == value:
                print("The required value was found at position: " + str(position))
                found = 1
                break
            if current.next == self.head:
                break
            current = current.next
        if found == 0:
            print("The required value does not exist in the list")
