class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val + '\n' + str(self.left) + '\n' + str(self.right)


def traverse_generate_string(node, string):
    if node is None:
        return string

    string += str(len(node.val))
    string += node.val

    if node.left is not None:
        string += '1'
        string = traverse_generate_string(node.left, string)
    else:
        string += '0'

    if node.right is not None:
        string += '1'
        string = traverse_generate_string(node.right, string)
    else:
        string += '0'

    return string


def serialize(root):
    return traverse_generate_string(root, '')


def generate_binary_tree(string, node):
    node.val = string[1: int(string[0])]

    string[int(string[0])]


def deserialize(string):
    assert(string)

    value = string[1: int(string[0]) + 1]
    leftover = string[int(string[0]) + 1:]

    node = Node(value)

    if leftover == '00':
        return node

    if int(leftover[0]) == 1:  # has left child
        node.left, leftover = deserialize(leftover[1:])

    if int(leftover[1]) == 1:  # has right child
        node.right = deserialize(leftover[2:])

    if int(leftover[0]) == 0 and int(leftover[1]) == 0:
        return (node, leftover[1:])

    return node


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(str(node))
print(serialize(node))
print('\n')
print(deserialize(serialize(node)))
assert deserialize(serialize(node)).left.left.val == 'left.left'
