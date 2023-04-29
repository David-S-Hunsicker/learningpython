def get_all_paths(n, edges):
    adj = {i: [] for i in range(1, n + 1)}
    results = []

    for src, dst in edges:
        adj[src].append(dst)

    def dfs(node, path):
        path.append(node)

        if path[-1] == n:
            results.append(path[:])
            path.pop()
            return

        for neighbor in adj[node]:
            dfs(neighbor, path)
        path.pop()

    dfs(1, [])
    return results
n = 4
edges = [
[1, 2],
[1, 3],
[2, 3],
[2, 4],
[3, 4]
]
print(get_all_paths(n, edges))