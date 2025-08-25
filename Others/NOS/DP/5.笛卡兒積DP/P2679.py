"""
P2679 [NOIP 2015 提高组] 子串
https://www.luogu.com.cn/problem/P2679
"""
MOD = int(1e9 + 7)
n, m, k = map(int, input().split())
A = input()
B = input()

# 4-Dimensional DP (MLE)
# f[i][j][t][0] 表示考慮 A 的前 i 個字元，已經選了 B 的前 j 個字元，選了 t 個子串，且最後一個字元不是/是子串的一部分的方案數
# f = [[[[0] * 2 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
# f[0][0][0][0] = 1
# for i in range(1, n + 1):
#     f[i][0][0][0] = 1
#     for j in range(1, m + 1):
#         for t in range(1, k + 1):
#             f[i][j][t][0] = (f[i - 1][j][t][0] + f[i - 1][j][t][1]) % MOD
#             if A[i - 1] == B[j - 1]:
#                 f[i][j][t][1] = (f[i - 1][j - 1][t][1] + f[i - 1][j - 1][t - 1][0] + f[i - 1][j - 1][t - 1][1]) % MOD
#             else:
#                 f[i][j][t][1] = 0
# print((f[n][m][k][0] + f[n][m][k][1]) % MOD)

# Rolling Array (TLE)
# f = [[[[0] * 2 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(2)]
# f[0][0][0][0] = 1
# for i in range(1, n + 1):
#     cur, pre = i & 1, (i - 1) & 1
#     f[cur][0][0][0] = 1
#     for j in range(1, m + 1):
#         for t in range(1, k + 1):
#             # 不選當前字元
#             f[cur][j][t][0] = (f[pre][j][t][0] + f[pre][j][t][1]) % MOD
#             # 選當前字元作為子串的一部分，可以是接在上一個子串的後面，也可以是獨立的子串
#             if A[i - 1] == B[j - 1]:
#                 f[cur][j][t][1] = (f[pre][j - 1][t][1] + f[pre][j - 1][t - 1][0] + f[pre][j - 1][t - 1][1]) % MOD
#             else:
#                 f[cur][j][t][1] = 0
# print((f[n & 1][m][k][0] + f[n & 1][m][k][1]) % MOD)

f = [[[0] * 2 for _ in range(k + 1)] for _ in range(m + 1)]
nf = [[[0] * 2 for _ in range(k + 1)] for _ in range(m + 1)]
for i in range(1, n + 1):
    f[0][0][0] = 1
    for j in range(1, m + 1):
        for t in range(1, k + 1):
            # 不選當前字元
            nf[j][t][0] = (f[j][t][0] + f[j][t][1]) % MOD
            # 選當前字元作為子串的一部分，可以是接在上一個子串的後面，也可以是獨立的子串
            if A[i - 1] == B[j - 1]:
                nf[j][t][1] = (f[j - 1][t][1] + f[j - 1][t - 1][0] + f[j - 1][t - 1][1]) % MOD
            else:
                nf[j][t][1] = 0
    f, nf = nf, f
print((f[m][k][0] + f[m][k][1]) % MOD)