# Topological sort orders traversal for Directed Acyclic Graphs
def top_sort(n, edges):
    order = []
    visited = [False] * n
    adj_list = [[] for _ in range(n)]
    for src, dst in edges:
        adj_list[src].append(dst)

    def sort(node):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                sort(neighbor)
        order.append(node)
    for node in range(n):
        if not visited[node]:
            sort(node)
    order.reverse()
    return order
n = 5
edges = [
    [0,1],
    [0,3],
    [1,2],
    [2,3],
    [2,4],
    [3,4]
]

print(top_sort(n, edges))