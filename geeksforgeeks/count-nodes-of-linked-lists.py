def getCount(self, head_node):
    # code here
    if head_node is None:
        return 0
    else:
        count = 0
        cur = head_node
        while cur:
            count += 1
            cur = cur.next
        return count
