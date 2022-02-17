def search(self, val):
    if self.root is None:
        return -1
    cur = self.root
    while cur:
        if cur.val == val:
            return cur.val

        if val < cur.val:
            cur = cur.left
        else:
            cur = cur.right

    else:
        return -1
