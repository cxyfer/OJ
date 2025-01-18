"""
貪心，考慮可能的買法需要花的硬幣數：
1. 用 1 個 10 元買 1 瓶，需要 1 個硬幣
2. 用 2 個 5 元買 1 瓶，需要 2 個硬幣
3. 用 3 個 1 元和 1 個 5 元買 1 瓶，需要 4 個硬幣
4. 用 3 個 1 元和 1 個 10 元買 1 瓶，需要 4 個硬幣
5. 用 8 個 1 元買 1 瓶，需要 8 個硬幣
"""
from collections import defaultdict

memo = defaultdict(lambda: float('inf'))
def dfs(k, a, b, c):
    if k == 0:
        return 0
    if memo[(k, b, c)] != float('inf'):
        return memo[(k, b, c)]
    res = float('inf')
    if a >= 3 and b >= 1:
        res = min(res, dfs(k - 1, a - 3, b - 1, c) + 4)
    if b >= 2:
        res = min(res, dfs(k - 1, a + 2, b - 2, c) + 2)
    if c >= 1:
        res = min(res, dfs(k - 1, a + 2, b, c - 1) + 1)
    if a >= 3 and c >= 1:
        res = min(res, dfs(k - 1, a - 3, b + 1, c - 1) + 4)
    if res == float('inf'):
        res = 8 * k
    memo[(k, b, c)] = res
    return res

t = int(input().strip())

for _ in range(t):
    k, a, b, c = map(int, input().strip().split())
    print(dfs(k, a, b, c))