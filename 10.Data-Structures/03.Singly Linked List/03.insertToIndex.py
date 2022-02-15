def insertToIndex(self, val, index):
    if index <= 0 or self.length < index:
        print("Out of index!")
    else:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            current = self.head
            count = 0
            while current.next is not None:
                if count == index - 1:
                    break

                current = current.next
                count += 1
            temp = current.next
            current.next = node
            node.next = temp
            self.length += 1
