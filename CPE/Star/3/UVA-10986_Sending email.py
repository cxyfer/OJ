import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

from heapq import *

T = int(input())
answer = []
for kase in range(1, T + 1):
    n, m, s, t = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    dist = [float('inf')] * n
    dist[s] = 0
    hp = [(0, s)]
    while hp:
        d, u = heappop(hp)
        if u == t:
            answer.append(f'Case #{kase}: {d}')
            break
        if d > dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(hp, (nd, v))
    else:
        answer.append(f'Case #{kase}: unreachable')
print("\n".join(answer))