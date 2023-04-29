def is_it_a_tree(node_count, edge_start, edge_end):
    visited = [False] * node_count
    adjList = [[] for _ in range(node_count)]
    parent = [-1] * node_count

    # build adjacency list
    for i in range(len(edge_start)):
        adjList[edge_start[i]].append(edge_end[i])
        adjList[edge_end[i]].append(edge_start[i])

    # search
    def dfs(node):
        visited[node] = True
        for neighbor in adjList[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                if not dfs(neighbor):
                    return False
            else:
                if neighbor != parent[node]:
                    return False
        return True

    # a tree requires only one DFS

    if not dfs(0):
        return False

    # multicomponent detection
    for i in range(len(visited)):
        if not visited[i]:
            return False
    return True


node_count = 4
edge_start = [0, 2, 0]
edge_end = [3, 1, 1]

print(is_it_a_tree(node_count, edge_start, edge_end))

# node_count= 4
# edge_start= [0, 0, 0]
# edge_end=[1, 2, 3]
# print(is_it_a_tree(node_count, edge_start, edge_end))
