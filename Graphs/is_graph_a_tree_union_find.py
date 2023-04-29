class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


def is_it_a_tree(node_count, edge_start, edge_end):
    if len(edge_start) != node_count - 1:
        return False  # A tree must have exactly n-1 edges

    # Initialize a UnionFind data structure with n nodes
    uf = UnionFind(node_count)

    # Union nodes that are connected by an edge
    for i in range(len(edge_start)):
        start = edge_start[i]
        end = edge_end[i]
        if uf.find(start) == uf.find(end):
            return False  # A cycle was found
        uf.union(start, end)

    # Check if all nodes are in the same connected component
    return len(set(uf.find(x) for x in range(node_count))) == 1


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