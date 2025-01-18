"""
    題意為在 a 和 b 中由前往後選擇字元，使得與 c 的差異最小。

    首先考慮由前往後推，定義 dfs(i, j) 為 a 已經選擇 i 個字元，b 已經選擇 j 個字元的最小差異。
    則此時有兩種選擇：
        1. 選 a[i]，得 dfs(i + 1, j) + (a[i] != c[i + j])
        2. 選 b[j]，得 dfs(i, j + 1) + (b[j] != c[i + j])
    兩者取最小值即可。最後取 dfs(0, 0) 做為入口。

    也可以由後往前反推，定義 dfs(i, j) 為 a 還有 i 個字元未選，b 還有 j 個字元未選的最小差異。
"""

t = int(input())

for _ in range(t):
    a = input().strip()
    b = input().strip()
    c = input().strip()

    m, n = len(a), len(b)

    # @cache
    # def dfs(i, j):
    #     if i == m and j == n:
    #         return 0
    #     res = float('inf')
    #     if i < m:
    #         res = min(res, dfs(i + 1, j) + (a[i] != c[i + j]))
    #     if j < n:
    #         res = min(res, dfs(i, j + 1) + (b[j] != c[i + j]))
    #     return res
    # print(dfs(0, 0))

    f = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
    f[m][n] = 0
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i < m:
                f[i][j] = min(f[i][j], f[i + 1][j] + (1 if a[i] != c[i + j] else 0))
            if j < n:
                f[i][j] = min(f[i][j], f[i][j + 1] + (1 if b[j] != c[i + j] else 0))
    print(f[0][0])