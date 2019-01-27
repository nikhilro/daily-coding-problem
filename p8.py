class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val) + ' ' + str(self.left) + ' ' + str(self.right)


def count_unival(node):
    if node is None:
        return 0, True
    if node.left is None and node.right is None:
        return 1, True

    left_count, is_left_unival = count_unival(node.left)
    right_count, is_right_unival = count_unival(node.right)

    if is_left_unival and is_right_unival:
        if (node.left is not None and node.left.val != node.val) \
                or (node.right is not None and node.right.val != node.val):
            return left_count + right_count, False
        else:
            return left_count + right_count + 1, True
    else:
        return left_count + right_count, False


root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print(count_unival(root))


# Wrong attempts as forgot to return boolean of itself being unival
# def count_unival(node):
#     if node is None:
#         return 0
#     if node.left is None and node.right is None:
#         return 1

#     left_count = count_unival(node.left)
#     right_count = count_unival(node.right)

#     if node.left is not None and node.right is not None \
#             and node.left.val == node.right.val == node.val:
#         return left_count + right_count + 1
#     elif node.left is None and node.right.val == node.val:
#         return left_count + right_count + 1
#     elif node.right is None and node.left.val == node.val:
#         return left_count + right_count + 1
#     else:
#         return left_count + right_count


# root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
# print(count_unival(root))


# def count_unival_golf(node):
#     if node is None:
#         return 0
#     if node.left is None and node.right is None:
#         return 1

#     left_count = count_unival(node.left)
#     right_count = count_unival(node.right)

#     if (node.left is not None and node.left.val != node.val) \
#             or (node.right is not None and node.right.val != node.val):
#         return left_count + right_count
#     else:
#         return left_count + right_count + 1


# root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
# print(count_unival_golf(root))
