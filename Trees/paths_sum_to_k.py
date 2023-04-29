class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Only ROOT to LEAF paths are valid
def all_paths_sum_k(root, k):
    paths = []

    def dfs(root, path, target):
        if not root: return
        # add on to path
        path.append(root.value)
        if target - root.value == 0 and not root.left and not root.right:
            paths.append(path[:])

        dfs(root.left, path, target - root.value)
        dfs(root.right, path, target - root.value)
        path.pop()

    dfs(root, [], k)
    return paths if len(paths) > 0 else [[-1]]

root = BinaryTreeNode(10)
root.left = BinaryTreeNode(25)
root.left.left = BinaryTreeNode(45)
root.right = BinaryTreeNode(30)
root.right.left = BinaryTreeNode(40)
root.right.right = BinaryTreeNode(50)

print(all_paths_sum_k(root, 80))