def invert(node):
    if node is None:
        return node
    node.left, node.right = invert(node.right), invert(node.left)
    return node 
    
    