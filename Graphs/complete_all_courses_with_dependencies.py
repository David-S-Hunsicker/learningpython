def can_be_completed(n, a, b) -> bool:
    visited = [0] * n
    '''
    0 : unvisited
    1 : in current path
    2 : visited
    '''
    adj = [[] for i in range(n)]
    # build adj
    for i in range(len(a)):
        adj[a[i]].append(b[i])
    def dfs(node)-> bool:
        visited[node] = 1 # active
        for neighbor in adj[node]:
            if visited[neighbor] == 1: return False
            elif visited[neighbor] == 0:
                if not dfs(neighbor): return False
        visited[node] = 2 # completed processing
        return True
    for i in range(n):
        if visited[i] == 0:
            if not dfs(i): return False
    return True

n=4
a= [1, 1, 3]
b= [0, 2, 1]
print(can_be_completed(n,a,b))