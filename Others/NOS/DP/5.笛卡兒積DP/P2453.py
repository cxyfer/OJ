"""
P2453 [SDOI2006] 最短距离
https://www.luogu.com.cn/problem/P2453

注意此題給定的 s 和 t 有額外的空白字元
注意 kill 操作是應用在後綴上，如果用前綴定義狀態的話要另外處理
"""
s = input().strip()
t = input().strip()
dlt, rep, cpy, ins, twi = map(int, input().split())
n, m = len(s), len(t)

def solve1(s: str, t: str):  # Memoization
    from functools import cache
    import sys
    sys.setrecursionlimit(int(1e3))
    # f(i, j)：將源串的「後綴」 s[i:] 轉換為目標串的「後綴」 t[j:] 所需的最小代價。
    @cache
    def f(i: int, j: int) -> int:
        if i == n and j == m:
            return 0
        if i == n:
            return (m - j) * ins
        if j == m:
            return (n - i) * dlt - 1
        res = min(f(i + 1, j) + dlt, f(i, j + 1) + ins, f(i + 1, j + 1) + rep)
        if cpy < rep and s[i] == t[j]:
            res = min(res, f(i + 1, j + 1) + cpy)
        if i < n - 1 and j < m - 1 and s[i] == t[j + 1] and s[i + 1] == t[j]:
            res = min(res, f(i + 2, j + 2) + twi)
        return res
    print(f(0, 0))

def solve2(s: str, t: str):  # Memoization
    from functools import cache
    import sys
    sys.setrecursionlimit(int(1e3))
    # f(i, j)：將源串的「前綴」 s[:i+1] 轉換為目標串的「前綴」 t[:j+1] 所需的最小代價。
    @cache
    def f(i: int, j: int) -> int:
        if i < 0 and j < 0:
            return 0
        if i < 0:
            return (j + 1) * ins
        if j < 0:
            return (i + 1) * dlt
        res = float('inf')
        res = min(res, f(i - 1, j) + dlt, f(i, j - 1) + ins, f(i - 1, j - 1) + rep)
        if cpy < rep and s[i] == t[j]:
            res = min(res, f(i - 1, j - 1) + cpy)
        if i > 0 and j > 0 and s[i] == t[j - 1] and s[i - 1] == t[j]:
            res = min(res, f(i - 2, j - 2) + twi)
        return res
    ans = f(n - 1, m - 1)
    for i in range(n - 2, -1, -1):
        ans = min(ans, f(i, m - 1) + (n - 1 - i) * dlt - 1)
    print(ans)

solve1(s, t)
# solve2(s, t)