
def BFS_average(self):
    if self.root is None:
        return []

    data = []
    queue = [self.root]
    while len(queue):
        hegith = []
        length = len(queue)
        for i in range(length):
            current = queue.pop(0)
            hegith.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        data.append(hegith)

    ans = []
    for item in data:
        avg = sum(item) / len(item)
        ans.append(avg)

    return ans
