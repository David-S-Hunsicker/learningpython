class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def largest_bst(root):
    def helper(node):
        if not node:
            # use inf as a min value cuz we take the min of it
            # use -inf as a max value cuz we take the max of it
            #      tree count,      min,       max
            return True, 0, float('inf'), float('-inf')

        left_is_bst, left_size, left_min, left_max = helper(node.left)
        right_is_bst, right_size, right_min, right_max = helper(node.right)

        if left_is_bst and right_is_bst and left_max < node.value < right_min:
            return True, 1 + left_size + right_size, min(left_min, node.value), max(right_max, node.value)
        else:
            return False, max(left_size, right_size), None, None

    _, largest_bst_size, _, _ = helper(root)
    return largest_bst_size


# Example usage:
# Construct a binary tree
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Find the size of the largest BST in the binary tree
print(largest_bst(root))  # Output: 3
