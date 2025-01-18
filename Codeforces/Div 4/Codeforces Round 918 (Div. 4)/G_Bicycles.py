from collections import deque
import heapq

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    S = [0] + list(map(int, input().split()))

    g = [[] for _ in range(N+1)]
    W = [[float('inf')] * (N+1) for _ in range(N+1)]
    for u, v, w in edges:
        W[u][v] = min(W[u][v], w)
        W[v][u] = min(W[v][u], w)
        g[u].append(v)
        g[v].append(u)
    for i in range(1, N+1):
        W[i][i] = 0

    # Dijkstra
    # 會有特別繞路去拿車的情況
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    visited = [False] * (N+1)
    parent = [0] * (N+1) # 紀錄最短路徑上的前一個點
    bike = [0] * (N+1)
    bike[1] = S[1]
    queue = [(0, 1)]

    while queue:
        cur_dist, u = heapq.heappop(queue)
        if dist[u] < cur_dist:
            continue
        # 繞路拿車
        min_bike = bike[u]
        min_bike_idx = 0
        for v in g[u]:
            if min_bike > S[v]:
                min_bike = S[v]
                min_bike_idx = v
        extra_cost = W[u][min_bike_idx] * (bike[u] + min_bike)

        for v in g[u]:
            d1 = dist[u] + W[u][v] * bike[u]
            d2 = dist[u] + W[u][v] * min_bike + extra_cost if min_bike < bike[u] else float('inf')
            if d2 < d1:
                if dist[v] > d2:
                    dist[v] = d2
                    parent[v] = u
                    bike[v] = min(min_bike, S[v])
                    heapq.heappush(queue, (dist[v], v))
                    continue
            else:
                if dist[v] > d1:
                    dist[v] = d1
                    parent[v] = u
                    bike[v] = min(bike[u], S[v])
                    heapq.heappush(queue, (dist[v], v))
                    continue
    print(dist[N])
