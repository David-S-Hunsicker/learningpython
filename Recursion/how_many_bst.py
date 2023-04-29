def how_many_bsts(n):
    def count_subtrees(start, end):
        if start > end:
            return 1
        count = 0
        root = start
        while root <= end:
            count += count_subtrees(start, root - 1) * count_subtrees(root + 1, end)
            root += 1
        return count

    return count_subtrees(1, n)

# This creates a triangle of repeating answers that reference previously solved problems.
# Because it's a counting problem it could be solved in quadratic time using a 1d array.
