def findMin(self):
    if self.root is None:
        return "Not found!"
    else:
        cur = self.root
        prev = cur
        while cur:
            prev = cur
            cur = cur.left
        return prev.val
