# does not auto balance
def build_a_bst(values):
    root = BinaryTreeNode(values[0])

    def insert(val):
        prev = None
        cur = root

        # find empty leaf
        while cur != None:
            prev = cur
            if val > cur.value:
                cur = cur.right
            else:
                cur = cur.left

        if val > prev.value:
            prev.right = BinaryTreeNode(val)
        else:
            prev.left = BinaryTreeNode(val)

    for i in range(1, len(values)):
        insert(values[i])
    return root