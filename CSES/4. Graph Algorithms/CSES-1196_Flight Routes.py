from heapq import *

n, m, k = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))

ans = []
cnt = [0] * n
hp = [(0, 0)] # (dist, node)
while hp:
    d, u = heappop(hp)
    if u == n - 1 and cnt[u] >= k:
        break
    if (cnt[u] >= k):
        continue
    cnt[u] += 1
    if u == n - 1:
        ans.append(d)
    for v, w in g[u]:
        heappush(hp, (d + w, v))
# print(*ans)
print(" ".join(map(str, ans)))