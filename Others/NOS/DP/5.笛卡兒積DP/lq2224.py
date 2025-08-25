"""
LQ2224 [2022 国赛] 修路
https://www.lanqiao.cn/problems/2224/learning/
"""
import math

n, m, d = map(int, input().split())
A = [0] + list(map(int, input().split())) + [float("inf")]
B = [0] + list(map(int, input().split())) + [float("inf")]
A.sort()
B.sort()

f = [[[float("inf")] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
f[0][0][0] = 0
for i in range(1, n + 1):
    # f[i][0][0] = f[i - 1][0][0] + A[i] - A[i - 1]
    f[i][0][0] = A[i]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j][0] = min(f[i - 1][j][0] + A[i] - A[i - 1],
                         f[i - 1][j][1] + math.hypot(A[i] - B[j], d))
        f[i][j][1] = min(f[i][j - 1][1] + B[j] - B[j - 1],
                         f[i][j - 1][0] + math.hypot(A[i] - B[j], d))
print(f"{min(f[n][m][0], f[n][m][1]):.2f}")