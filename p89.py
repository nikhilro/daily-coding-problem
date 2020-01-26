import math

def validate_bst(root, left_bound=-math.inf, right_bound=math.inf):
    if root == None:
        return True 

    return (
        left_bound <= root.key <= right_bound 
        and validate_bst(root.left, left_bound=left_bound, right_bound=root.key)
        and validate_bst(root.right, left_bound=root.key, right_bound=right_bound)
    )