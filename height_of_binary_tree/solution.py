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


def height(root):
    from collections import deque

    # Use level order traversal to count levels
    def count_levels(root_node):
        levels = 0
        # Since level order traversal is breadth-first traversal, we will use
        # a queue to maintain the nodes that need to be traversed
        queue = deque([root_node])

        # We'll append child nodes of the nodes within the queue so that
        # we can determine that a level has changed once the queue is emptied
        temp_queue = deque()

        # Traverse till the queue is empty
        while len(queue) or len(temp_queue):
            # Try popping a node from the queue
            try:
                node = queue.pop()
            except IndexError:
                # The queue is empty, thus level change
                levels += 1

                # Transfer contents of temp_queue into queue
                queue, temp_queue = temp_queue, queue
                continue

            # Add child nodes to the temp_queue
            if node.left:
                temp_queue.appendleft(node.left)
            if node.right:
                temp_queue.appendleft(node.right)

        return levels

    num_of_levels = count_levels(root)

    return num_of_levels

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
