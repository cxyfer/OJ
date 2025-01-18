"""
    Python TLE
"""
a, b = map(int, input().split())

# dp[x][y] 表示將 x * y 的矩形切成所有正方形的最小切割次數
f = [[float("inf")] * (b + 1) for _ in range(a + 1)]
for x in range(1, min(a, b) + 1):
    f[x][x] = 0

for x in range(1, a + 1):
    for y in range(1, b + 1):
        for k in range(1, x):
            f[x][y] = min(f[x][y], f[k][y] + f[x - k][y] + 1)
        for k in range(1, y):
            f[x][y] = min(f[x][y], f[x][k] + f[x][y - k] + 1)
print(f[a][b])