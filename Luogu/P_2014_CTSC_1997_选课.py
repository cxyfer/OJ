n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
W = [0] * (n + 1)
for v in range(1, n + 1):
    u, w = map(int, input().split())
    g[u].append(v)
    W[v] = w

# f[u][k] 表示以 u 為根的子樹中選 k 門課的最大價值
f = [[0] * (m + 1) for _ in range(n + 1)]
def dfs(u):
    sz = 1
    f[u][0] = 0 # 不選課
    # 先假設不選 u 這門課
    for v in g[u]:
        v_sz = dfs(v)
        sz += v_sz
        # 分組背包
        for k in range(min(sz, m), 0, -1): # 枚舉 u 子樹選課數量，為了避免覆蓋尚未計算的狀態，從大到小枚舉
            for i in range(1, min(k, v_sz) + 1): # 枚舉 v 子樹選課數量
                f[u][k] = max(f[u][k], f[u][k - i] + f[v][i])
    if u != 0:
        # 一定要選 u 這門課，所以選 k 門課是原本的 k - 1 門課加上 u 這門課
        for k in range(m, 0, -1):
            f[u][k] = f[u][k - 1] + W[u]
    return sz

dfs(0)
print(f[0][m])