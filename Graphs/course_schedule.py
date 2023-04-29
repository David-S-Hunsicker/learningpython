
def course_schedule(n, prerequisites):
    r = []
    visited = [False] * n
    finished = [False] * n
    adj_list = [[] for _ in range(n)]
    def build_adj():
        for course, dep in prerequisites:
            adj_list[course].append(dep) # directed

    def dfs_no_back_edge(node):
        visited[node] = True
        # recursive logic
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if not dfs_no_back_edge(neighbor):
                    return False
            else: # already visited
                if not finished[neighbor]: # back edge
                    return False
        finished[node] = True
        r.append(node)
        return True

    build_adj()
    # explore all components
    for i in range(len(visited)):
        if not visited[i]:
            if not dfs_no_back_edge(i):
                return [-1]
    return r


n= 4
prerequisites= [
[1, 0],
[2, 0],
[3, 1],
[3, 2]
]
print(course_schedule(n, prerequisites))