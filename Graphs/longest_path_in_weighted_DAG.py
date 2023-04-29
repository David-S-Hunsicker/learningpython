def find_highest_weight_path(num_nodes, sources, destinations, weights, start_node, end_node):
    # Initialize distances and parents arrays
    distances = [-float('inf') for _ in range(num_nodes)]
    parents = [-1 for _ in range(num_nodes)]
    distances[start_node] = 0

    # Create adjacency list
    adj_list = {i: [] for i in range(num_nodes)}
    for i in range(len(sources)):
        adj_list[sources[i]].append((destinations[i], weights[i]))

    # Topologically sort the graph
    def topological_sort(node, visited, stack):
        visited.add(node)
        for neighbor, weight in adj_list[node]:
            if neighbor not in visited:
                topological_sort(neighbor, visited, stack)
        stack.append(node)

    stack = []
    visited = set()
    for i in range(num_nodes):
        if i not in visited:
            topological_sort(i, visited, stack)
    stack.reverse()

    # Traverse nodes in topological order
    for node in stack:
        for neighbor, weight in adj_list[node]:
            new_distance = distances[node] + weight
            if new_distance > distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = node

    # Construct path from start to end node
    path = []
    node = end_node
    while node != -1:
        path.append(node)
        node = parents[node]
    path.reverse()

    # Return highest weight path and path of nodes traversed
    return (distances[end_node], path)
