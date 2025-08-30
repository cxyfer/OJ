def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    ans = [0] * n
    dep = [-1] * n
    sz = [1] * n
    def dfs1(u: int, fa: int) -> None:
        # dep[u] = dep[fa] + 1
        # ans[0] += dep[u]
        # for v in g[u]:
        #     if v == fa:
        #         continue
        #     dfs1(v, u)
        #     sz[u] += sz[v]
        st = [(u, fa, 0)]  # (u, fa, i)
        while st:
            u, fa, i = st.pop()
            if i == 0:
                dep[u] = dep[fa] + 1
                ans[0] += dep[u]
            if i > 0:
                v = g[u][i - 1]
                sz[u] += sz[v]
            for j in range(i, len(g[u])):
                v = g[u][j]
                if v == fa:
                    continue
                st.append((u, fa, j + 1))
                st.append((v, u, 0))
                break
    dfs1(0, -1)

    def dfs2(u: int, fa: int) -> None:
        # for v in g[u]:
        #     if v == fa:
        #         continue
        #     ans[v] = ans[u] + (n - sz[v]) - sz[v]
        #     dfs2(v, u)
        st = [(u, fa, 0)]
        while st:
            u, fa, i = st.pop()
            for j in range(i, len(g[u])):
                v = g[u][j]
                if v == fa:
                    continue
                ans[v] = ans[u] + (n - sz[v]) - sz[v]
                st.append((u, fa, j + 1))
                st.append((v, u, 0))
                break
    dfs2(0, -1)
    print(*ans)

if __name__ == "__main__":
    solve()