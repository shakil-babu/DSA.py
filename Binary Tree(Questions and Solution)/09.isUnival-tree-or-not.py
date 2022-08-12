def isUnivalTree(self, root):
    if root is None :
        return False
    
    data = []
    
    def traverse(node):
        if node.left :
            traverse(node.left)
            
        data.append(node.val)
        
        if node.right :
            traverse(node.right)
            
    traverse(root)
    
    first = data[0]
    for item in data :
        if item != first :
            return False
    return True
