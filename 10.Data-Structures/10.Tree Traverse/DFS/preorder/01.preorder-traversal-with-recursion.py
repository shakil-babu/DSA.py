def pre_order(self):
    if self.root == None:
        return

    print(self.root.val)
    pre_order(self.root.left)
    pre_order(self.root.right)
