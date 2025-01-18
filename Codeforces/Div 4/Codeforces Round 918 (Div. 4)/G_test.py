import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if dist[cur_node] < cur_dist:
            continue

        for neighbor, weight in graph[cur_node].items():
            distance = cur_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return dist