def rangeSumBST(self, root, low, high):
    if root is None :
        return 0
    
    ans , queue = 0, []
    queue.append(root)
    while len(queue) > 0 :
        cur = queue.pop(0)
        if cur.val >= low and high >= cur.val:
            ans += cur.val
        if cur.left : queue.append(cur.left)
        if cur.right : queue.append(cur.right)
    
    return ans
