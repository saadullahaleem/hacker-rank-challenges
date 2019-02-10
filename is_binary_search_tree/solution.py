""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# This is a bad solution.
# There is no need to traverse the complete Tree
# Just check each traversed element with the last traversed.
# If any of them is smaller than the last traversed one, it isn't a binary tree.

def in_order_traversal(node, values):
    if node.left:
        in_order_traversal(node.left, values)
    values.append(node.data)
    if node.right:
        in_order_traversal(node.right, values)


def checkBST(root):
    values = []
    in_order_traversal(root, values)
    return sorted(set(values)) == values
