import heapq
from collections import defaultdict

from queue import PriorityQueue

def prim_mst(graph):
    start_vertex = next(iter(graph))
    visited = {start_vertex}
    mst = []
    edges = PriorityQueue([(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]])

    while edges:
        weight, u, v = edges.get()
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    edges.put((weight, v, neighbor))

    return mst
'''
# This solution doesn't use kruskals or primm's algorithm
def minimum_cost(n_cities, connections):
    visited = set()
    distances = {i: float('inf') for i in range(1, n_cities + 1)}
    adj = defaultdict(list)

    # add adjacencies by weight, destination
    for src, dst, cost in connections:
        adj[src].append((cost, dst))
        adj[dst].append((cost, src))

    # look at a node's adjacencies, if put them in the heap
    # if the node's been visited then just continue
    # get the cheapest path off the heap, if in visited then just continue,
    # else check if it's cheaper, update accordingly and dfs

    heap = []

    # root is always 1
    def shortest_path(node):
        heapq.heappush(heap, (0, node))

        while heap:
            distance, node = heapq.heappop(heap)
            if node in visited: continue
            visited.add(node)
            if distance < distances[node]:
                distances[node] = distance
            for distance, neighbor in adj[node]:
                heapq.heappush(heap, (distance, neighbor))

    def dfs(node):
        visited.add(node)
        for distance, neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # find the root, or the node that can reach the whole graph
    for node in range(1, n_cities):
        if node not in visited:
            root = node
            dfs(node)

    # if the graph converges it can be done from this node, if it can't return -1
    visited = set()
    dfs(node)
    if len(visited) < n_cities: return -1

    # Find the min distance to each node based on the root's perspective
    visited = set()
    distances[root] = 0
    shortest_path(root)
    return sum(distances.values())
'''

n_cities = 5
connections = [
[1, 2, 3],
[1, 3, 1],
[1, 4, 4],
[1, 5, 10],
[2, 3, 5],
[2, 4, 2],
[2, 5, 3],
[3, 4, 6],
[3, 5, 2],
[4, 5, 2]
]
print(minimum_cost(n_cities, connections))