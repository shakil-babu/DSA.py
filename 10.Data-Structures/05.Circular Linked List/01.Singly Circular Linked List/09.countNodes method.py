def countNodes(self):
    count = 1
    if self.head is None:
        return 0
    else:
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count
