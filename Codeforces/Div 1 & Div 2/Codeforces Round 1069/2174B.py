"""
CF2174B - Wishing Cards
https://codeforces.com/contest/2174/problem/B

令 f[i][u][s] 表示考慮前 i 個朋友，最終的最大值為 u，使用了 s 張卡片時所能得到的最大快樂值。
則有 f[i][u][s] = max(f[i - 1][v][s - u] + (u - v) * (n - idx) for v in range(u))
可以寫出 O(n*k^3) 的 DP 做法。

注意到只有前綴最大值的位置才有意義，因此我們可以將 n 壓縮到 O(k)，得到 O(k^4) 的 DP 做法。

上述轉移需要枚舉 O(k) 的 v 值，考慮將其優化掉。注意到 u * (n - idx) 是定值，因此可以將其提出來，得到：
f[i][u][s] = u * (n - idx) + max(f[i - 1][v][s - u] - v * (n - idx) for v in range(u))
當 u - 1 -> u 的時候，只需要額外考慮 v = u - 1 的情況，因此轉移時可以壓縮到 O(1)。

可以用滾動陣列的方式空間優化，但 Python 需要把滾動陣列也優化掉。
由於轉移來源是 f[i - 1][v][s - u]，因此從 s 小到大更新，便可以保證轉移來源的值已經被更新過。
"""
def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert n == len(A)

    B = []
    for i, x in enumerate(A):
        if not B or x > B[-1][1]:
            B.append((i, x))

    # f[i][u][s] 表示考慮前 i 個有效的朋友，最終的最大值為 u，使用了 s 容量時的最大快樂值
    # f[i][u][s] = max(f[i - 1][v][s - u] + (u - v) * (n - idx) for v in range(u))

    # @cache
    # def dfs(i: int, u: int, s: int) -> int:
    #     if i < 0:
    #         return 0 if s >= 0 else -float('inf')
    #     idx, x = B[i]
    #     res = dfs(i - 1, u, s)  # 不選擇當前朋友
    #     if u <= x:  # 可以選擇當前朋友作為最大值 u
    #         for v in range(u):  # 枚舉前一個位置的最大值 v，其中 0 代表沒有前一個位置
    #             res = max(res, dfs(i - 1, v, s - u) + (u - v) * (n - idx))
    #     return res
    # print(max(dfs(m - 1, u, k) for u in range(k + 1)))

    f = [[float('-inf')] * (k + 1) for _ in range(k + 1)]
    for s in range(k + 1):
        f[0][s] = 0
    for idx, x in B:
        for s in range(k + 1):
            mx = float('-inf')  # 維護 max(f[v][s - u] - v * (n - idx) for v in range(u))
            for u in range(min(x, s) + 1):  # 只枚舉可能的 u 值
                w = u * (n - idx)
                ns = s - u
                if f[u][ns] < mx + w:
                    f[u][ns] = mx + w
                if mx < f[u][s] - w:
                    mx = f[u][s] - w
    print(max(map(max, f)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()