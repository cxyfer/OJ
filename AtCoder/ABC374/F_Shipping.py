import sys
from functools import cache
from itertools import accumulate
sys.setrecursionlimit(10000)

N, K, X = map(int, input().split())
T = list(map(int, input().split()))

s = list(accumulate(T, initial=0))

# dfs(i, j) 表示考慮到前 i 個貨物(即已發送 i 個貨物)，且上一次發貨時間為 j 的最小總成本
@cache
def dfs(i, j):
    if i == N:
        return 0
    res = float('inf')
    # 枚舉這次發貨的貨物數量
    for k in range(1, min(K + 1, N - i + 1)):
        # 這次發貨的時間，至少是上一次發貨的時間 + X 或 這批貨物的最晚發貨時間
        nxt_j = max(j + X, T[i + k - 1])
        # sum_{x=i}^{i+k-1} (nxt_j - T_x)
        # = k * nxt_j - sum_{x=i}^{i+k-1} T_x = k * nxt_j - (s[i + k] - s[i])
        sum_T = s[i + k] - s[i]
        cur = k * nxt_j - sum_T + dfs(i + k, nxt_j)
        res = min(res, cur)
    return res

ans = dfs(0, -float('inf'))
print(ans)