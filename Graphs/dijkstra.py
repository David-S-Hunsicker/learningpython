import heapq


def dijkstra(adj_list, start):
    # initialize distance dictionary and heap
    dist = {node: float('inf') for node in adj_list}
    dist[start] = 0
    heap = [(0, start)]

    # main loop
    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > dist[curr_node]:
            continue  # already processed
        for neighbor, weight in adj_list[curr_node].items():
            new_dist = dist[curr_node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist
