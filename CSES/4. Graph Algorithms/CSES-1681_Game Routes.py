from collections import deque

MOD = int(1e9 + 7)

n, m = map(int, input().split())

g = [[] for _ in range(n)]
ind = [0] * n
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    ind[v] += 1

f = [0] * n
f[0] = 1
q = deque([u for u in range(n) if ind[u] == 0])
while q:
    u = q.popleft()
    for v in g[u]:
        f[v] = (f[v] + f[u]) % MOD
        ind[v] -= 1
        if ind[v] == 0:
            q.append(v)

print(f[n - 1])