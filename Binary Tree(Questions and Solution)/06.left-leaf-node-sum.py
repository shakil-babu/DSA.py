def sumOfLeftLeaves(self, root):
        if root is None :
            return 0
        
        queue = []
        queue.append(root)
        s = 0
        while len(queue) > 0 :
            cur = queue.pop()
            if cur.left: 
                queue.append(cur.left)
                if not cur.left.left and not cur.left.right :
                    s += cur.left.val
            if cur.right: queue.append(cur.right)
                                
                
        return s
