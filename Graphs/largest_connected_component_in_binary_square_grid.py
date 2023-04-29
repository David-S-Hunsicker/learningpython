from collections import deque


def largest_connected_component(grid):
    component_sizes = {}
    component_index = 2  # 0 and 1 are initial values in grid

    n = len(grid)
    zeroes = []

    def bfs(row, col, index):
        component_size = 1
        grid[row][col] = index
        q = deque([(row, col)])
        while q:
            r, c = q.popleft()

            for (x, y) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if x >= 0 and y >= 0 and x <= n - 1 and y <= n - 1 and grid[x][y] == 1:
                    q.append((x, y))
                    component_size += 1
                    grid[x][y] = index
        return component_size

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                zeroes.append((i, j))
            elif grid[i][j] == 1:  # unvisited
                component_sizes[component_index] = bfs(i, j, component_index)
                component_index += 1

    max_component = 0
    if len(zeroes) == 0: return n ** 2
    if len(zeroes) == n ** 2: return 1
    for r, c in zeroes:
        size = 1
        neighbor_components = set()
        for (m, k) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if m >= 0 and k >= 0 and m <= n - 1 and k <= n - 1 and grid[m][k] > 0:
                neighbor_components.add(grid[m][k])

        for component in neighbor_components:
            size += component_sizes[component]

        max_component = max(max_component, size)

    return max_component


grid = [
    [1, 1],
    [1, 1]
]
print(largest_connected_component(grid))
