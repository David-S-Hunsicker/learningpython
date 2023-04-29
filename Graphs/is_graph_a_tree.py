
def is_it_a_tree(node_count, edge_start, edge_end):
    visited = set()
    adj_list = {}

    # build adjacency list
    for i in range(len(edge_start)):
        start = edge_start[i]
        end = edge_end[i]
        if start not in adj_list: adj_list[start] = []
        if end not in adj_list: adj_list[end] = []
        adj_list[start].append(end)
        adj_list[end].append(start)

    # search
    def dfs(node, parent = None):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor == parent: continue
            if neighbor in visited: return False
            if not dfs(neighbor, node): return False
        return True

    return dfs(edge_start[0]) and len(visited) == node_count


# example 1: a tree with 5 nodes and 4 edges
node_count = 5
edge_start = [0, 1, 2, 2]
edge_end = [1, 2, 3, 4]
print(is_it_a_tree(node_count, edge_start, edge_end))  # should print True

# example 2: a non-tree with 5 nodes and 5 edges
node_count = 5
edge_start = [0, 1, 2, 3, 2]
edge_end = [1, 2, 3, 4, 0]
print(is_it_a_tree(node_count, edge_start, edge_end))  # should print False

# example 3: a disconnected graph with 5 nodes and 4 edges
node_count = 5
edge_start = [0, 1, 2, 2]
edge_end = [1, 2, 3, 4]
# add a disconnected node to the graph
edge_start.append(5)
edge_end.append(6)
print(is_it_a_tree(node_count + 1, edge_start, edge_end))  # should print False

# example 4: a graph with a self-loop
node_count = 3
edge_start = [0, 1, 2, 1]
edge_end = [1, 2, 0, 1]
print(is_it_a_tree(node_count, edge_start, edge_end))  # should print False

# example 5: a graph with duplicate edges
node_count = 4
edge_start = [0, 1, 2, 1, 1]
edge_end = [1, 2, 3, 3, 0]
print(is_it_a_tree(node_count, edge_start, edge_end))  # should print False

