def display(self, node):

    ans = []
    if node is None:
        return node

    else:
        cur = node
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
