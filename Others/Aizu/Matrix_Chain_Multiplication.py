n = int(input())
p = []
for _ in range(n):
    a, b = map(int, input().split())
    if not p:
        p.append(a)
    p.append(b)

# dp[i][j] 表示從第 M_i 到 M_j 的最小乘法次數
dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]

# 初始化
for i in range(n + 1):
    dp[i][i] = 0

for ln in range(2, n + 1): # 枚舉長度
    for i in range(1, n + 1 - (ln - 1)): # 枚舉起點
        j = i + ln - 1 # 終點
        for k in range(i, j): # 枚舉分割點 [i, j)
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j])
            
print(dp[1][n])