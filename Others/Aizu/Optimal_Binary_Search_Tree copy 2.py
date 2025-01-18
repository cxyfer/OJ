n = int(input())
P = [0] + list(map(float, input().split())) #     k1, k2, ..., kn
Q = list(map(float, input().split()))       # d0, d1, d2, ..., dn

# 令 T[i][j] 表示包含 k_i 到 k_j 的樹，且令 T[i][i-1] 為空樹
# 令 f[i][j] 表示包含 k_i 到 k_j 的 OBST 的期望成本
f = [[0 for _ in range(n+2)] for _ in range(n+2)]
# 令 w[i][j] 表示包含 k_i 到 k_j 的 OBST 的累積機率
w = [[0 for _ in range(n+2)] for _ in range(n+2)]
# 令 m[i][j] 表示包含 k_i 到 k_j 的 OBST 的根的位置
m = [[0 for _ in range(n+2)] for _ in range(n+2)]

# 初始化 f[i][i-1] = q[i-1]（空樹的期望成本）
for i in range(1, n+2):
    f[i][i-1] = Q[i-1]
    w[i][i-1] = Q[i-1]
    m[i][i-1] = i  # 根的位置初始化為 i

# 計算累積機率 w[i][j]
for i in range(1, n+1):
    for j in range(i, n+1):
        w[i][j] = w[i][j-1] + P[j] + Q[j]

# for row in w:
#     print(*list(map(lambda x: f"{x:05.2f}", row)))

# 動態規劃計算 e[i][j]
for ln in range(1, n + 1):  # 子樹的長度
    for i in range(1, n - ln + 2):
        j = i + ln -1
        f[i][j] = float('inf')
        for k in range(i, j + 1):
            cost = f[i][k-1] + f[k+1][j] + w[i][j]
            if cost < f[i][j]:
                f[i][j] = cost
                m[i][j] = k
print(f"{f[1][n]:.8f}")