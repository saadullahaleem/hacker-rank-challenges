from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def level_order_traversal(root):
    # Since level order traversal is breadth-first traversal, we will use
    # a queue to maintain the nodes that need to be traversed
    queue = deque([root])

    # Traverse till the queue is empty
    while len(queue):
        # Pop a node from the queue
        node = queue.pop()
        print(node, end=' ')

        # Add child nodes to the queue in-order
        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

level_order_traversal(tree.root)
