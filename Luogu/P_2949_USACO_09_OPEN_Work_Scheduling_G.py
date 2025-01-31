from heapq import heappush, heappop
from collections import defaultdict

n = int(input())
G = defaultdict(list)
ans = 0
for _ in range(n):
    d, p = map(int, input().split())
    G[d].append(p)
hp = []
for k, ps in sorted(G.items()):
    for p in ps:
        heappush(hp, p)
        ans += p
        if len(hp) > k:
            ans -= heappop(hp)
print(ans)