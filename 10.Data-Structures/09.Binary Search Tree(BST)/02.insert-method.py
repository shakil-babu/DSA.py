def insert(self, val):
    node = Node(val)
    if self.root is None:
        self.root = node
        return
    else:
        current = self.root
        while True:
            if val == current.val:
                return
            if current.val < val:
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right

            elif current.val > val:
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
