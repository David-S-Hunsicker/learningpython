# does the tree have a root to leaf path that sums to k?
def path_sum(root, k):
    def dfs(node, target):
        if not node: return False # root can be None
        if target == 0: return True
        if dfs(node.left, target - node.value): return True
        if dfs(node.right, target - node.value): return True
        return False
    return dfs(root, k)


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def path_sum_2(root, k):
    def dfs(node, target):
        if not node.left and not node.right: return target - node.value == 0
        if node.left and dfs(node.left, target - node.value): return True
        if node.right and dfs(node.right, target - node.value): return True
        return False
    return dfs(root, k)