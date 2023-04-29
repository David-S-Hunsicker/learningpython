def find_basins(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    basins = [[-1] * cols for _ in range(rows)]
    basin_count = 0

    def get_basin(r, c):
        nonlocal basin_count, basins
        if basins[r][c] != -1:
            return basins[r][c]

        lowest_cell = matrix[r][c]
        min_row, min_col = r, c
        for row, col in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if row >= 0 and col >= 0 and row < rows and col < cols and matrix[row][col] < lowest_cell:
                lowest_cell = matrix[row][col]
                min_row, min_col = row, col

        # This cell is a basin
        if min_row == r and min_col == c:
            basin = basin_count
            basin_count += 1
        else: # Find this cells basin
            basin = get_basin(min_row, min_col)

        basins[r][c] = basin
        return basin

    basin_counts = [0]
    for r in range(rows):
        for c in range(cols):
            basin = get_basin(r, c)
            if basin == len(basin_counts):
                basin_counts.append(0)
            basin_counts[basin] += 1

    return sorted(basin_counts, reverse=True)


matrix = [
[1, 5, 2],
[2, 4, 7],
[3, 6, 9]
]
print(find_basins(matrix))