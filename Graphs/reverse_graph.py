def reverse_graph(n, edges):
    adj_map = [[] for _ in range(n)]
    for src, dst in edges:
        adj_map[dst].append(src)
    return adj_map
edges = [[0, 1],[1,2],[4,4],[3,4]]

print(reverse_graph(5, edges))