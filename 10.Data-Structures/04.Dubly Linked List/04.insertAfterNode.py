# insertAfterNode
def insertAfterNode(self, val, newVal):
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
            node.next = current.next
            node.prev = current

            if current.next is not None:
                current.next.prev = node
            current.next = node
