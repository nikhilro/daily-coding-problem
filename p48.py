from collections import deque

class Node:
    def __init__(self, val=None, right=None, left=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return "\n ({} -> l: {} -> r: {})".format(self.val, str(self.left), str(self.right))
    
def construct_tree(inorder, preorder): 
    inorder, preorder = deque(inorder), deque(preorder)

    def traverse(parent=None):
        if not preorder or not inorder:
            return 
        cur = Node(preorder.popleft(), parent=parent)
        cur.left = traverse(cur) if inorder[0] != cur.val else inorder.popleft() and None
        if inorder:
            cur.right = traverse(cur) if inorder[0] != parent.val and inorder[0] != parent.parent.val else inorder.popleft() and None
        return cur
    
    return traverse(Node(parent=Node()))

print(construct_tree(['d', 'b', 'e', 'a', 'f', 'c', 'g'], ['a', 'b', 'd', 'e', 'c', 'f', 'g']))


def construct_tree_2(inorder, preorder):
    if not preorder:
        return
    root = Node(preorder[0])
    if inorder:
        switch_in = inorder.index(preorder[0])
        switch_pre = preorder.index(inorder[switch_in - 1])
        root.left = construct_tree_2(inorder[:switch_in], preorder[1: switch_pre + 1])
        root.right = construct_tree_2(inorder[switch_in + 1:], preorder[switch_pre + 1:])
    return root

print(construct_tree_2(['d', 'b', 'e', 'a', 'f', 'c', 'g'], ['a', 'b', 'd', 'e', 'c', 'f', 'g']))
