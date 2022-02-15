def insertBeforeNode(self, val, newVal):
    node = Node(newVal)
    if self.head is None:
        print("DLL is empty!")
    else:
        current = self.head
        while current is not None:
            if current.val == val:
                break
            current = current.next

        if current is None:
            print("Node is not found!")
        else:
            node.next = current
            node.prev = current.prev

            if current.prev is not None:
                current.prev.next = node
            else:
                self.head = node
            current.prev = node
