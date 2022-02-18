def BFS(self):
    if self.root is None:
        return []

    data = []
    queue = [self.root]
    while len(queue):
        current = queue.pop(0)
        data.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return data
