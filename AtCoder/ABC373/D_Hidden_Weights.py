from collections import deque

N, M = map(int, input().split())

edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u-1, v-1, w))

g = [[] for _ in range(N)]
indeg = [0] * N
for u, v, w in edges:
    g[u].append((v, w))
    g[v].append((u, -w))
    indeg[v] += 1

ans = [0] * N 
vis = [False] * N
for i in range(N):
    if vis[i]:
        continue
    vis[i] = True
    q = deque([i])
    rq = deque([i])
    while q:
        u = q.popleft()
        for v, w in g[u]:
            if not vis[v]:
                vis[v] = True
                ans[v] = ans[u] + w
                q.append(v)
                rq.append(v)
            else:
                if ans[v] != ans[u] + w:
                    raise Exception
print(*ans)
