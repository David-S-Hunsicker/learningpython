import math
import heapq


def nearest_neighbours(p_x, p_y, k, n_points):
    heap = []

    def distance(n_x, n_y) -> float:
        return math.sqrt((n_x - p_x) ** 2 + (n_y - p_y) ** 2)

    for i in range(len(n_points)):
        n_x, n_y = n_points[i]
        d = distance(n_x, n_y)
        heapq.heappush(heap, (-d, n_points[i]))
        if len(heap) > k: heapq.heappop(heap)

    heap = [heap[i][1] for i in range(len(heap))]
    return heap

p_x = 1
p_y = 1
n_points = [
[0, 0],
[1, 0]
]
print(nearest_neighbours(p_x, p_y, 1, n_points))