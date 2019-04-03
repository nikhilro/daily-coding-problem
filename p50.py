class Node:
    def __init__(self, right, left, val):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "({} -> l: {} -> r: {})".format(self.val, str(self.left), str(self.right))

def evaluate(node): # O(n) time, O(n) space (stack), not tested
    if '0' < node.val < '9':
        return node.val
    
    left, right = evaluate(node.left), evaluate(node.right)
    return eval("{} {} {}".format(left, node.val, right))