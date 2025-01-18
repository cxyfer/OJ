from heapq import heappush, heappop

MOD = int(1e9 + 7)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))

dist = [float('inf')] * n
cnt = [0] * n
minf = [0] * n
maxf = [0] * n
dist[0] = 0
cnt[0] = 1
minf[0] = 0
maxf[0] = 0

hp = [(0, 0)] # (dist, node)
while hp:
    d, u = heappop(hp)
    if d > dist[u]:
        continue
    if u == n - 1:
        break
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            cnt[v] = cnt[u]
            minf[v] = minf[u] + 1
            maxf[v] = maxf[u] + 1
            heappush(hp, (nd, v))
        elif nd == dist[v]:
            cnt[v] = (cnt[v] + cnt[u]) % MOD
            maxf[v] = max(maxf[v], maxf[u] + 1)
            minf[v] = min(minf[v], minf[u] + 1)
 
print(dist[n - 1], cnt[n - 1], minf[n - 1], maxf[n - 1])