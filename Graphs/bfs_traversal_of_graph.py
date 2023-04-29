import queue


def bfs(result, adjList, node, visited):
    q = queue.Queue()
    q.put(node)

    while not q.empty():
        node = q.get()
        visited[node] = True
        result.append(node)
        for i in adjList[node]:
            if not visited[i]:
                visited[i] = True
                q.put(i)


def bfs_traversal(n, edges):
    if n == 1:
        return [0]

    visited = [False] * n
    r = []

    # build adjacency list
    adjList = [[] for x in range(n)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])

    for i in range(len(visited)):
        if not visited[i]:
            bfs(r, adjList, i, visited)
    return r

n= 4
edges= [
[0, 1],
[0, 2],
[1, 3],
[1, 2],
]
print(bfs_traversal(n, edges))