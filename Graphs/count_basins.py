from collections import defaultdict


def find_basins(matrix):
    # every cell tries to find the lowest
    # if a cell sees itself is the lowest then it adds itself to basins dictionary (cell x, y : count)
    # if a cell has a neighbor that has is in flow_to (x ,y ) ( lowest_x, lowest_y) then it takes that and increments lowest(x,y)
    flow_to = {}
    basins = defaultdict(int)

    def get_neighbors(cell):
        x, y = cell
        possible = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        neighbors = []
        for n_x, n_y in possible:
            if n_x >= 0 and n_y >= 0 and n_x < len(matrix) and n_y < len(matrix[x]):
                neighbors.append((n_x, n_y))
        return neighbors

    def find_basin(cell):
        lowest = cell
        neighbors = get_neighbors(cell)
        for neighbor in neighbors:
            if matrix[neighbor[0]][neighbor[1]] < matrix[lowest[0]][lowest[1]]:  # neighbor is lower
                lowest = neighbor
        if lowest == cell:  # this cell is a basin
            return cell
        else:
            flow_to[cell] = find_basin(lowest)
            return flow_to[cell]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            basin = find_basin((row, col))
            # if (row, col) not in basins:
            basins[basin] += 1

    results = []
    for key, values in basins.items():
        results.append(values)

    return sorted(results)


grid = [
    [0, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 3, 3, 3],
    [5, 5, 2, 1]
]
# [4, 5, 7]
print(find_basins(grid))
