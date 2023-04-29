"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def postorder_traversal(root):
    if not root:
        return []
    stack = [root]
    results = []
    visited = set()

    while stack:
        node = stack[-1]
        if node in visited:
            results.append(node.value)
            stack.pop()
        else:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            visited.add(node)

    return results
