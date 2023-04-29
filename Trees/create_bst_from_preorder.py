import sys


# this only works when the tree maintains the BST imperitive
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_search_tree(preorder):
    def create_tree(lower_bound, upper_bound):
        nonlocal index
        # We only need n nodes, backtrack to prevent out of bounds.
        if index == n: return

        root_value = preorder[index]
        # Every node has a lower and upper bound based on parent node
        # If we're outside bounds we've gone too deep into the preorder
        if root_value < lower_bound or root_value > upper_bound:

        # Reduce and conquer
        root = BinaryTreeNode(root_value)
        index += 1

        # Attempt to create child nodes while respecting the binary search tree imperative.
        root.left = create_tree(lower_bound, root_value)  # left child must be less than root.value
        root.right = create_tree(root_value, upper_bound)  # right child must be greater than root.value
        return root

    index = 0;
    n = len(preorder)
    return create_tree(-sys.maxsize, sys.maxsize)
preorder = [2,0,1,3,5,4]
print(build_binary_search_tree(preorder))