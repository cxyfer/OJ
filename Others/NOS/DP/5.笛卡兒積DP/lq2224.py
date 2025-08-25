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

# @cache
# def f(i: int, j: int, is_A: bool) -> int:
#     if i == n and j == m:
#         return 0
#     if i > n or j > m:
#         return float("inf")
#     if is_A:
#         return min(f(i + 1, j, True) + A[i + 1] - A[i],
#                    f(i, j + 1, False) + math.hypot(A[i] - B[j + 1], d))
#     else:
#         return min(f(i, j + 1, False) + B[j + 1] - B[j],
#                    f(i + 1, j, True) + math.hypot(A[i + 1] - B[j], d))
# print(f"{f(0, 0, True):.2f}")

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