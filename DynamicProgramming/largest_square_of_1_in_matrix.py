# matrix implementation
def largest_sub_square_matrix(n, m, mat):
    # create a table bigger than the matrix
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    largest = 0
    for row in range(1, n+1):
        for col in range(1, m+1):
            if mat[row-1][col-1] == 1:
                # if we have a 1, look up, left, and diagonal
                table[row][col] = min(table[row-1][col], table[row][col-1], table[row-1][col-1]) +1
                largest = max(largest, table[row][col])
    return largest

# two row implementation
def largest_sub_square_matrix(n, m, mat):
    # create a table bigger than the matrix
    table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    largest = 0

    last = [0] * (m + 1)
    for row in range(1, n + 1):
        cur = [0] * (m + 1)
        for col in range(1, m + 1):
            if mat[row - 1][col - 1] == 1:
                # if we have a 1, look up, left, and diagonal
                cur[col] = min(last[col], cur[col - 1], last[col - 1]) + 1
                largest = max(largest, cur[col])
        last = cur
    return largest