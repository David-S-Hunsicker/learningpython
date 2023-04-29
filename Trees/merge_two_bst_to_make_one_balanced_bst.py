##### IT's far faster if we just use the nodes don't create new ones and just look at the node values in our arrays

# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def merge_two_binary_search_trees(root1, root2):
    if not root1: return root2
    if not root2: return root1

    def dfs(node):
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
        vals.append(node.value)

    def create_order(arr):
        if not arr: return
        mid = len(arr) // 2
        node = BinaryTreeNode(arr[mid])
        node.left = create_order(arr[:mid])
        node.right = create_order(arr[mid + 1:])
        return node

    vals = []
    dfs(root1)
    dfs(root2)
    vals.sort()
    return create_order(vals)

### This version uses a linear time sort because of in order traversal rather than using nlogn sort
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def merge_two_binary_search_trees(root1, root2):
    if not root1: return root2
    if not root2: return root1

    def dfs(node, vals):
        if node.left:
            dfs(node.left, vals)
        vals.append(node.value)
        if node.right:
            dfs(node.right, vals)

    def create_tree(arr):
        if not arr: return
        mid = len(arr) // 2
        node = BinaryTreeNode(arr[mid])
        node.left = create_tree(arr[:mid])
        node.right = create_tree(arr[mid + 1:])
        return node

    def merge_orders(l_arr, r_arr):  # linear sort instead of timsort since we did inorder traversal
        left, right = 0, 0
        vals = []
        while left < len(l_arr) and right < len(r_arr):
            if l_arr[left] < r_arr[right]:
                vals.append(l_arr[left])
                left += 1
            else:
                vals.append(r_arr[right])
                right += 1
        vals += l_arr[left:]
        vals += r_arr[right:]
        return vals

    vals1 = []
    dfs(root1, vals1)
    vals2 = []
    dfs(root2, vals2)
    vals = merge_orders(vals1, vals2)
    return create_tree(vals)
