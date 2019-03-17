import math

class Node:
    def __init__(self, val, left, right):
        self.val = val 
        self.left = left
        self.right = right
    
# def max_vals_naive(root): # not tested, O(n) time
#     if not root:
#         return -math.inf
#     vals = list(max_vals_naive(root.left) + max_vals_naive(root.right) + root.val)
#     max_val = max(vals)
#     max_i = vals.index(max_val)
#     return max_val, max(vals[:max_i] + vals[max_i + 1:])

# def second_largest(root): # not tested, O(n) time, O(1) space
#     largest, second_largest, cur_node = root.val, None, root
#     while cur_node.right:
#         largest, second_largest = root.right, largest
#     return second_largest

def largest_iterator(node): # O(n) for full traversal, O(1) space
    if node.right:
        yield from largest_iterator(node.right)

    if node.left:
        yield from largest_iterator(node.left)
    
    yield node.val 

def second_largest(root): # O(h) where h = height of tree
    it = largest_iterator(root)
    
    return next(next(it))