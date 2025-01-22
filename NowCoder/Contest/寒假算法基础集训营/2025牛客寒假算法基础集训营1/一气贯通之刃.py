n = int(input())

g = [[] for _ in range(n)]
deg = [0] * n
for _ in range(n-1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

ans = []
for i, d in enumerate(deg):
    if d == 1:
        ans.append(i + 1)
    elif d < 1 or d > 2:
        print(-1)
        break
else:
    print(*ans if len(ans) == 2 else -1)