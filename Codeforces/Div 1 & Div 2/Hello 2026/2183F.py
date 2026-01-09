MOD = 998244353

def solve():
    n = int(input())
    s = input().strip()

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    dfn = [0] * n
    sz = [1] * n
    order = []
    time = 0
    def dfs(u, fa):
        nonlocal time
        # dfn1[u] = time
        # order.append(u)
        # time += 1
        # for v in g[u]:
        #     if v == fa:
        #         continue
        #     dfs(v, u)
        #     sz[u] += sz[v]
        st = [(u, fa, 0)]
        while st:
            u, fa, i = st.pop()
            if i == 0:
                dfn[u] = time
                order.append(u)
                time += 1
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
    dfs(0, -1)

    # suf[i][j] = sum(f[i][j] for i in [i, n) for j in [j, n))
    suf = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        u = order[i]
        r1 = i + sz[u]
        for j in range(n - 1, -1, -1):
            v = order[j]
            r2 = j + sz[v]
            # if s[u] == s[v], f[i][j] = 1 + sum(f[i][j] for i in [i+1, r1) for j in [j+1, r2))
            # where [i+1, r1) is the subtree of u and [j+1, r2) is the subtree of v
            if s[u] == s[v]:
                f = (1 + suf[i + 1][j + 1] - suf[r1][j + 1] - suf[i + 1][r2] + suf[r1][r2]) % MOD
            # else, f[i][j] = 0
            else:
                f = 0
            # suf[i][j] = f[i][j] + suf[i+1][j] + suf[i][j+1] - suf[i+1][j+1]
            suf[i][j] = (f + suf[i + 1][j] + suf[i][j + 1] - suf[i + 1][j + 1]) % MOD

    ans = [0] * n
    for u in range(n):
        l, r = dfn[u], dfn[u] + sz[u]
        ans[u] = (suf[l][l] - suf[r][l] - suf[l][r] + suf[r][r]) % MOD
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()