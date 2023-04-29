def convert_edge_list_to_adjacency_matrix(n, edges):
    matrix = [[False]  * n for _ in range(n)]
    for i in range(len(edges)):
        matrix[edges[i][0]][edges[i][1]] = True
        matrix[edges[i][1]][edges[i][0]] = True
    return matrix

n = 2
edges= [
[0, 1]
]
print(convert_edge_list_to_adjacency_matrix(n, edges))