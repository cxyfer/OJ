from heapq import *

n, m = map(int, input().split())

# 路徑圖
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))

# 依賴圖，需要先完成 u 才能完成 g[u]
ind = [0] * n
g2 = [[] for _ in range(n)]
for u in range(n):
    x, *nodes = map(lambda x: int(x), input().split())
    ind[u] = x
    for v in nodes:
        g2[v - 1].append(u)

# Dijkstra
hp = [(0, 0)] # (dist, u)
dist = [float('inf')] * n
dist[0] = 0
cnt = 0
while hp:
    d, u = heappop(hp)
    if d > dist[u]:
        continue
    # 考慮路徑圖
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            # 更新距離，但不受依賴的才加入堆
            dist[v] = nd
            if ind[v] == 0:
                heappush(hp, (nd, v))

    # 考慮依賴圖
    for v in g2[u]:
        # 因為 v 依賴 u，所以 v 的距離至少要等於 u 的距離
        dist[v] = max(dist[v], dist[u])
        ind[v] -= 1
        # 如果 v 的依賴已經完成，則加入堆
        if ind[v] == 0:
            heappush(hp, (dist[v], v))

print(dist[n - 1])