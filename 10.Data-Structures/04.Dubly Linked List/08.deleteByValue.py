# delete by value
def deleteByValue(self, val):
    if self.head is None:
        print("Dll is empty!")
        return

    if self.head.next is None:
        if self.head.val == val:
            self.head = None
            self.tail = None
        else:
            print("Node not found!")
        return

    if self.head.val == val:
        self.head = self.head.next
        self.head.prev = None

    else:
        current = self.head
        while current is not None:
            if current.val == val:
                break
            current = current.next
        if current.next is not None:
            current.next.prev = current.prev
            current.prev.next = current.next
        else:
            if current.val == val:
                current.prev.next = None
            else:
                print("Node not present!")
