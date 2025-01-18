n = int(input())

g = [[] for _ in range(n)]
fa = [-1] + list(map(lambda x: int(x) - 1, input().split()))
for i in range(1, n):
    g[fa[i]].append(i)

ans = [0] * n

# def dfs(u):
#     res = 0
#     for v in g[u]:
#         dfs(v)
#         res += ans[v] + 1
#     ans[u] = res
#     return
# dfs(0)

st = [(0, True)]
while st:
    u, flag = st.pop()
    if flag:
        st.append((u, False))
        for v in g[u]:
            st.append((v, True))
    else:
        res = 0
        for v in g[u]:
            res += ans[v] + 1
        ans[u] = res

print(*ans)