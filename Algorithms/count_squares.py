class DetectSquares:

    def __init__(self):
        self.grid = [[0 for _ in range(50)] for _ in range(50)]

    def add(self, point: list[int]) -> None:
        self.grid[point[0]][point[1]] += 1

    def get_x_values_of_y(self, px, py):
        results = []
        for x in range(len(self.grid)):
            if x == px:
                continue

            if self.grid[x][py] > 0:
                results.append(x)
        return results

    # find all the points at the same y-axis as the count point
    # check if there are two corresponding points on any x-axis
    def count(self, point: list[int]) -> int:
        px, py = point
        y_vals = self.get_x_values_of_y(px, py)
        squares = 0
        # check every y value and point along every other x-axis and see if there's any squares
        for y in y_vals:
            for x in range(len(self.grid)):
                if x == px:
                    continue

                if self.grid[x][y] > 0 and self.grid[x][py] > 0:
                    # found a square, count it
                    squares += self.grid[x][y] * self.grid[x][py] * self.grid[px][y]

        return squares


detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
print(detectSquares.count([11, 10]))

print(detectSquares.count([14, 8]))
detectSquares.add([11, 2])
print(detectSquares.count([11, 10]))
