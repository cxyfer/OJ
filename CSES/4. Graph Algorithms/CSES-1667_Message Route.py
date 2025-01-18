from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

vis = [False] * n
pre = [-1] * n
vis[0] = True
q = deque([0])
while q:
    u = q.popleft()
    for v in g[u]:
        if vis[v]:
            continue
        vis[v] = True
        pre[v] = u
        q.append(v)

if pre[n - 1] == -1:
    print("IMPOSSIBLE")
else:
    ans = []
    x = n - 1
    while x != -1:
        ans.append(x + 1)
        x = pre[x]
    ans.reverse()
    print(len(ans))
    print(*ans)