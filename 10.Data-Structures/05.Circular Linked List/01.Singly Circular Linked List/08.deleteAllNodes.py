def deleteAllNodes(self):
    if self.head is None:
        print("List is emtpy!")
    else:
        cur = self.head
        while cur.next != self.head:
            temp = cur.next
            cur = None
            cur = temp
        self.head = None
