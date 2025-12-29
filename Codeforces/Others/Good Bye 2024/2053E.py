from collections import deque

def solve():
    n = int(input())

    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    q = deque([u for u in range(n) if deg[u] == 1])
    dist = [0 if deg[u] == 1 else float('inf') for u in range(n)]
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                q.append(v)

    cnt = [0] * 3
    for u in range(n):
        cnt[min(dist[u], 2)] += 1

    sz = [0] * n
    f = [0] * n

    def dfs(u, fa):
        # sz[u] = 1 if dist[u] > 1 else 0
        # for v in g[u]:
        #     if v == fa:
        #         continue
        #     dfs(v, u)
        #     sz[u] += sz[v]
        #     if dist[v] == 1:
        #         f[u] += sz[v]
        st = [(u, fa, 0)]
        while st:
            u, fa, i = st.pop()
            if i == 0:
                sz[u] = 1 if dist[u] > 1 else 0
            if i > 0:
                v = g[u][i - 1]
                sz[u] += sz[v]
                if dist[v] == 1:
                    f[u] += sz[v]
            for j in range(i, len(g[u])):
                v = g[u][j]
                if v == fa:
                    continue
                st.append((u, fa, j + 1))
                st.append((v, u, 0))
                break

    def reroot(u, fa):
        # for v in g[u]:
        #     if v == fa:
        #         continue
        #     if dist[u] == 1:
        #         f[v] += (cnt[2] - sz[v])
        #     reroot(v, u)
        st = [(u, fa, 0)]
        while st:
            u, fa, i = st.pop()
            for j in range(i, len(g[u])):
                v = g[u][j]
                if v == fa:
                    continue
                if dist[u] == 1:
                    f[v] += (cnt[2] - sz[v])
                st.append((u, fa, j + 1))
                st.append((v, u, 0))
                break

    dfs(0, -1)
    reroot(0, -1)

    ans = cnt[0] * (n - cnt[0])
    for u in range(n):
        if dist[u] >= 1:
            ans += f[u]

    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()