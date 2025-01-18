import sys
sys.setrecursionlimit(1 << 20)
from collections import defaultdict

while True:
    u, v, *rest = map(int, input().strip().split())
    if u == 0 and v == 0:
        break
    edges = [(u, v, rest[0])]
    while True:
        u, v, *rest = map(int, input().strip().split())
        if u == 0 and v == 0:
            break
        edges.append((u, v, rest[0]))

    g = defaultdict(list)
    deg = defaultdict(int)
    for u, v, eid in edges:
        g[u].append((v, eid))
        g[v].append((u, eid))
        deg[u] += 1
        deg[v] += 1

    if any(deg[u] & 1 for u in deg):
        print("Round trip does not exist.")
        print()
        continue

    for u in g:
        g[u].sort(key=lambda x: x[1]) # 按照邊的編號排序
 
    path = []
    used = set()
    def dfs(u):
        while g[u]:
            v, idx = g[u].pop(0)
            if idx in used:
                continue
            used.add(idx)
            dfs(v)
            path.append(idx)

    st = min(edges[0][0], edges[0][1]) # 從第一條邊的較小端點開始
    dfs(st)
    print(*path[::-1])
    print()