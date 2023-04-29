def maximum_path_sum(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row > 0 and col > 0:
                grid[row][col] += max(grid[row - 1][col], grid[row][col - 1])
            elif row > 0:
                grid[row][col] += grid[row - 1][col]
            elif col > 0:
                grid[row][col] += grid[row][col - 1]

    return grid[-1][-1]


grid= [
[4, 5, 8],
[3, 6, 4],
[2, 4, 7]
]

print(maximum_path_sum(grid))