import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

n, m, q = map(int, input().split())

g = [[float('inf')] * n for _ in range(n)]
for u in range(n):
    g[u][u] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    g[u][v] = min(g[u][v], w)
    g[v][u] = min(g[v][u], w)

for k in range(n):
    for i in range(n):
        if i == k or g[i][k] == float('inf'):
            continue
        for j in range(n):
            if j == k or g[k][j] == float('inf'):
                continue
            nd = g[i][k] + g[k][j]
            if nd < g[i][j]:
                g[i][j] = nd

for _ in range(q):
    u, v = map(lambda x: int(x) - 1, input().split())
    print(g[u][v] if g[u][v] != float('inf') else -1)