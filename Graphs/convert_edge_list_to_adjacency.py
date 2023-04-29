
def convert_edge_list_to_adjacency_list(n, edges):
    if n <= 1:
        return [[]]
    adj = []
    for i in range(n):
        adj.append(list([]));
    for i in range(n):
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])
    return adj

edges = [
[0, 1],
[1, 4],
[1, 2],
[1, 3],
[3, 4]
]

n = 5
print(convert_edge_list_to_adjacency_list(n, edges))