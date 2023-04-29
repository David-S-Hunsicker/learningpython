def get_number_of_islands_after_each_operation(num_rows, num_cols, update_positions):
    island_parents = {}

    def find_island_parent(island):
        nonlocal island_parents
        while island != island_parents[island]:
            island_parents[island] = island_parents[island_parents[island]]
            island = island_parents[island]
        return island_parents[island]

    def union_islands(island1, island2):
        parent1 = find_island_parent(island1)
        parent2 = find_island_parent(island2)
        if parent2 != parent1:
            island_parents[parent1] = parent2

    # setup
    island_count = 0
    results = []
    # do the operations, set new island as its own parent, check neighbors and union, if so, decrement islands
    for row, col in update_positions:
        island_count += 1
        island_parents[(row, col)] = (row, col) # set the islands parent to itself
        for n_x, n_y in [(row-1, col),(row+1, col),(row, col-1),(row, col+1),]: # get neighbors
            # if the neighbor is valid and it's an island in our island map, join it to the neighbor
            if 0 <= n_x < num_rows and 0 <= n_y < num_cols and (n_x, n_y) in island_parents:
                union_islands((row, col), (n_x, n_y)) # merge them
                island_count -= 1 # decrease island count
        results.append(island_count)

    return results

numrows = 3
numcols = 3

updates = [
[0, 0],
[0, 2],
[0, 1],
[2, 1],
[1, 1]
]
print(get_number_of_islands_after_each_operation(numrows, numcols, updates))