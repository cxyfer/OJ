n, k = map(int, input().split())
P = [0] + list(map(int, input().split()))

vis = [False] * (n + 1)
res = [0] * (n + 1)

for u in range(1, n + 1):
    if vis[u]:
        continue
    cycle = []
    cur = u
    while not vis[cur]:
        vis[cur] = True
        cycle.append(cur)
        cur = P[cur]
    ln = len(cycle)
    moves = pow(2, k, ln)
    for i, v in enumerate(cycle):
        res[v] = cycle[(i + moves) % ln]

print(*res[1:])