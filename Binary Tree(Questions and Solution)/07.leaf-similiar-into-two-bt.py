def leafSimilar(self, root1, root2):
    def bfs(root):
        if root is None:
            return []

        if not root.left and not root.right :
            return [root.val]
        
        return bfs(root.left) + bfs(root.right)
        
    a = bfs(root1)
    b = bfs(root2)
    return a == b
