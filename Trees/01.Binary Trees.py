# Binary Trees:
# A type of tree in which a node have at-most 2 child nodes.

# Preorder Sequence List
nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]

# Values with - are null means no child nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A pointer which shows index num of list
index = 0

def binary_tree():
          global index
         # This is Recursive
          if index >= len(nodes):
              return None
          value = nodes[index]
          index = index + 1

          if value == -1:
              return None

          node = Node(value)

          node.left = binary_tree()
          node.right = binary_tree()

          return node

root = binary_tree()

def print_tree(node):
    if node is None:
        return
    print(node.data) # prints root node to verify the tree


print_tree(root)


