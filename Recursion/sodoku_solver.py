def solve_sudoku_puzzle(grid):
    row, col = find_empty_cell(grid)
    if row == -1 and col == -1:
        return True  # complete solution

    for val in range(1, 10):
        if is_valid_move(grid, row, col, val):
            grid[row][col] = val
            if solve_sudoku_puzzle(grid):  # recursive call
                return True
            grid[row][col] = 0  # all future moves invalid
    return False  # backtrack


def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return (-1, -1)


def is_valid_move(grid, row, col, val):
    # row check
    if val in grid[row]:
        return False
    # col check
    if val in [grid[i][col] for i in range(9)]:
        return False
    # box check
    box_row = (row // 3) * 3
    bow_col = (col // 3) * 3
    if val in [grid[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]:
        return False
