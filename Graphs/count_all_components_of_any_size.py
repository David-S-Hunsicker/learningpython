def number_of_connected_components(n, edges):
    visited = set()
    adj_list = {}
    component_count = 0

    # build directed adjacency map to prevent "dead-end" node problem
    for start, end in edges:
        if start not in adj_list:
            adj_list[start] = []
        adj_list[start].append(end)
        if end not in adj_list:
            adj_list[end] = []
        adj_list[end].append(start)

    def dfs(node):
        if node in visited: return
        visited.add(node)
        for neighbor in adj_list[node]:
            dfs(neighbor)

    visited = set()
    for start, end in edges:
        if start not in visited:
            dfs(start)
            component_count += 1

    # add in all the 1-node components
    component_count += n - len(adj_list)
    return component_count

n = 8
edges = [
[0, 1],
[2, 3],
[4, 5],
[6, 7],
[4, 7],
[5, 6]
]
print(number_of_connected_components(n, edges))