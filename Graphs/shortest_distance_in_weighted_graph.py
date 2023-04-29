import heapq

def dijkstra(node_count, edges, start):
    # build adjacency list
    adj_list = {i: {} for i in range(node_count)}
    for start_node, end_node, weight in edges:
        adj_list[start_node][end_node] = weight

    # initialize distances
    dist = {i: float('inf') for i in range(node_count)}
    dist[start] = 0

    # initialize heap
    heap = [(0, start)]

    # track size of component: initialized to 1 since we always have a start node
    found = 1

    # main loop
    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > dist[curr_node]:
            continue  # already processed
        for neighbor, weight in adj_list[curr_node].items():
            new_dist = dist[curr_node] + weight
            if new_dist < dist[neighbor]:
                if dist[neighbor] == float('inf'): found += 1
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    # at this point the shortest distance to every node in the component of the start node is calculated.
    # returning -1 means we can't get to every node in the graph, there are more than one component.
    return -1 if found < node_count else dist
# Test case 1
node_count = 4
edges = [(0, 1, 5), (0, 2, 2), (1, 2, 1), (1, 3, 3), (2, 3, 4)]
start = 0
print(dijkstra(node_count, edges, start))