n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(lambda x: int(x)-1, input().split())
    g[u].append(v)
    g[v].append(u)
k = int(input())
V = set(map(lambda x: int(x)-1, input().split()))

cnt = [0] * n
ans = [0] * n
vis = [False] * n

# def dfs(u, fa):
#     vis[u] = True
#     cnt[u] = 1 if u in st else 0
     
#     for v in g[u]:
#         if v == fa or vis[v]:
#             continue
#         dfs(v, u)
#         cnt[u] += cnt[v]
     
#     ans[u] = cnt[u] * cnt[u]
#     for v in g[u]:
#         if v == fa:
#             continue
#         ans[u] -= cnt[v] * cnt[v]
# dfs(0, -1)

st = [(0, -1, 0)]  # (u, fa, state)
while st:
    u, fa, state = st.pop()
    if state == 0:
        vis[u] = True
        cnt[u] = 1 if u in V else 0
        st.append((u, fa, 1))
        for v in g[u]:
            if v != fa and not vis[v]:
                st.append((v, u, 0))
    else:
        for v in g[u]:
            if v != fa:
                cnt[u] += cnt[v]
        ans[u] = cnt[u] * cnt[u]
        for v in g[u]:
            if v != fa:
                ans[u] -= cnt[v] * cnt[v]
print(*ans)