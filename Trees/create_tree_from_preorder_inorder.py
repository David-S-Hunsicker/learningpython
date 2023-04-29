
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"inorder": [3, 2, 1, 5, 4, 6]
"preorder":[1, 2, 3, 4, 5, 6]
"""
def construct_binary_tree(inorder, preorder):
    n = len(inorder)-1
    # We need to know how many nodes are left and right of any given node to build its subtree
    inorder_map = { val: i for i, val in enumerate(inorder) }

    def builder(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start > preorder_end: return

        # Make the root
        root_val = preorder[preorder_start]
        root_index = inorder_map[root_val]
        root = BinaryTreeNode(root_val)

        # How big are the left and right subtree?
        left_st = root_index - inorder_start
        right_st= inorder_end - root_index

        # Subtree    builder(preorder_start,           preorder_end,              inorder_start, inorder_end)
        root.left  = builder(preorder_start+1,         preorder_start + left_st,  inorder_start, root_index-1)
        root.right = builder(preorder_start+1+left_st, preorder_end,              root_index+1,  inorder_end)
        return root

    return builder(0, n, 0 ,n)