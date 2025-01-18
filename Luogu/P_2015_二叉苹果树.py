n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))

dp = [[0] * (q + 1) for _ in range(n)]
def dfs(u, fa):
    child = [(v, w) for v, w in g[u] if v != fa]
    if not child:
        return 0
    ls, lv = child[0]
    rs, rv = child[1]
    sz = dfs(ls, u) + dfs(rs, u) + 2
    for k in range(min(sz, q) + 1): # 枚舉在 u 的子樹中選 k 條邊
        for i in range(k + 1): # 枚舉左子樹選 i 條邊
            j = k - i # 右子樹選 j = k - i 條邊
            left = dp[ls][i - 1] + lv if i > 0 else 0 # 扣除 u 到 ls 和 rs 的邊
            right = dp[rs][j - 1] + rv if j > 0 else 0 
            dp[u][k] = max(dp[u][k], left + right)
    return sz

dfs(0, -1)
print(dp[0][q])