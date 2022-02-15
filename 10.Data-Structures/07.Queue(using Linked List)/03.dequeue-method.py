def dequeue(self):
    if self.head is None:
        print("queue is empty!")
        return
    else:
        deleteNode = self.head
        self.head = deleteNode.next
        self.length -= 1

        if self.length == 0:
            self.tail = None
