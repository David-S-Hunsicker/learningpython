def number_of_connected_components(n, edges):
    components = 0
    visited = [False] * n
    adjList = [[] for _ in range(n)]
    # fill the adjacency list
    for src, dst in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)

    def dfs(node):
        visited[node] = True
        for neighbor in adjList[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    # traverse the visited list and search the corresponding node every time it's not there. -> increment components
    for i in range(len(visited)):
        if not visited[i]:
            components += 1
            dfs(1)
    return components

edges = [
[0, 1],
[0, 2],
[0, 3],
[4, 5],
[4, 6],
[4, 7]
]
n = 8
print(number_of_connected_components(n, edges))