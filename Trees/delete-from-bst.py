def delete(root, parent, value):
    if root is None:
        return

    if value != root.value:
        if value < root.value:
            delete(root.left, root, value)
        else:
            delete(root.right, root, value)
    else:
        if root.left is None and root.right is None:  # no children, no witnesses.
            if parent is None:  # edge case of deleting the root of the tree
                root = None
                return
            if parent.left and parent.left.value == root.value:
                parent.left = None
            else:
                parent.right = None
        elif root.left and root.right:  # 2 children
            next = root.left
            while next.right:
                next = next.right
            root.value = next.value
            delete(root.left, root, next.value)
        else:  # 1 child
            if root.left:
                root.value = root.left.value
                root.left = root.left.left
            else:
                root.value = root.right.value
                root.right = root.right.right


def delete_from_bst(root, values):
    for i in range(len(values)):
        delete(root, None, values[i])
    return root
