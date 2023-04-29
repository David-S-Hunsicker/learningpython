def find_town_judge(n, trust):
    if n == 1:
        return 1

    # visited = [] * (n + 1)
    trusted = [0] * (n + 1)
    adjList = [[] for _ in range(n+1)]
    for truster, trustee in trust:
        adjList[truster].append(trustee)
        trusted[trustee] += 1
    # a judge should have a value of n-1 in trust[]
    for i in range(1, len(trusted)):
        if trusted[i] == n - 1:
            # a just should trust no one
            if len(adjList[i]) == 0:
                return i
    return -1


n = 2
trust = [
    [2, 1]
]
print(find_town_judge(n, trust))