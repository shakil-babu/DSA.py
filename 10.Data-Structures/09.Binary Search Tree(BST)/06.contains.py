
def contains(self, val):
    if self.root is None:
        return False
    cur = self.root
    while cur:
        if cur.val == val:
            return True

        if cur.val < val:
            cur = cur.right
        else:
            cur = cur.left

    return False
