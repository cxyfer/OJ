import sys
sys.setrecursionlimit(int(1e5))

MOD = int(1e9 + 7)

n = int(input())
A = list(map(int, input().split()))

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

ans = 0
for b in range(31):
    arr = [(x >> b) & 1 for x in A]

    # f[u][0/1] 表示以節點 u 為根的子樹中，
    # 所有「包含根節點 u」的連通分量中，第 b 位為 0/1 的節點個數總和（不同連通分量各計算一次）
    f = [[0, 0] for _ in range(n)]
    # s[u] 表示以節點 u 為根的子樹中，所有「包含根節點 u」的連通分量在第 b 位上的權值總和
    s = [0] * n
    # cnt[u] 表示以節點 u 為根的子樹中，包含節點 u 的連通分量數量
    cnt = [0] * n

    def dfs(u, fa):
        f[u][arr[u]] = 1
        cnt[u] = 1
        for v in g[u]:
            if v == fa:
                continue
            dfs(v, u)

            # Calculate f0 and f1 (count of 1's and 0's in all paths)
            f0 = (f[u][0] + f[u][0] * cnt[v] + cnt[u] * f[v][0]) % MOD
            f1 = (f[u][1] + f[u][1] * cnt[v] + cnt[u] * f[v][1]) % MOD

            # Update s[u] (count of pairs)
            s[u] = (s[u] * (cnt[v] + 1)
                    + f[u][0] * f[v][1]
                    + f[u][1] * f[v][0]
                    + s[v] * cnt[u]) % MOD

            # Update cnt[u] (number of solutions with u as LCA)
            cnt[u] = (cnt[u] * (1 + cnt[v])) % MOD

            f[u][0], f[u][1] = f0, f1

    dfs(0, -1)

    for i in range(n):
        ans = (ans + s[i] * (1 << b)) % MOD

print((ans * 2) % MOD)
