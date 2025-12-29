from functools import reduce

MOD = 998244353

MAX_N = int(2e5 + 5)
fact = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    fact[i] = (fact[i - 1] * i) % MOD

def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)

    comps = []
    sz = [0] * n
    def dfs(u, fa):
        # sz[u] = 1
        # for v in g[u]:
        #     if v == fa:
        #         continue
        #     dfs(v, u)
        #     if sz[v] & 1:
        #         sz[u] += sz[v]
        #     else:
        #         comps.append(sz[v])
        st = [(u, fa, 0)]
        while st:
            u, fa, i = st.pop()
            if i == 0:
                sz[u] = 1
            if i > 0:
                v = g[u][i - 1]
                if sz[v] & 1:
                    sz[u] += sz[v]
                else:
                    comps.append(sz[v])
            for j in range(i, len(g[u])):
                v = g[u][j]
                if v == fa:
                    continue
                st.append((u, fa, j + 1))
                st.append((v, u, 0))
                break
    dfs(0, -1)
    
    if len(comps) == 0:
        print(1)
        return

    ans = (sz[0] * fact[len(comps) - 1]) % MOD
    ans = (ans * reduce(lambda x, y: (x * y * y) % MOD, comps, 1)) % MOD
    ans = (ans * reduce(lambda x, y: (x + y) % MOD, map(lambda x: pow(x, MOD - 2, MOD), comps), 0)) % MOD
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()