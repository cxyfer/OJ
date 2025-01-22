from heapq import *

n, k, st, ed, x, y = map(int, input().split())
st, ed = st - 1, ed - 1

hp = [(0, st, k)]  # (dist, node, k)
dist = [float("inf")] * n
dist[st] = 0
while hp:
    d, u, k = heappop(hp)
    if d > dist[u]:
        continue
    if u == ed:
        print(d)
        break

    nxt = (u + x) % n
    if d + 1 < dist[nxt]:
        dist[nxt] = d + 1
        heappush(hp, (d + 1, nxt, k))

    nxt = (u - y) % n
    if d + 1 < dist[nxt]:
        dist[nxt] = d + 1
        heappush(hp, (d + 1, nxt, k))

    nxt = (u + n // 2) % n
    if k and d + 1 < dist[nxt]:
        dist[nxt] = d + 1
        heappush(hp, (d + 1, nxt, k - 1))
else:
    print(-1)