def levelOrder(self, root):

    queue = [root]
    result = []

    while len(queue) > 0:
        cur = queue.pop(0)
        result.append(cur.data)

        if cur.left:
            queue.append(cur.left)

        if cur.right:
            queue.append(cur.right)

    return result
