"""
由於要選 n 個數，因此其實每個 x = 0, 1, 2, ..., n - 1 都會選一個
考慮每個 x 平面上選擇哪個數字，維護 y_mask 和 z_mask 兩個狀態表示已經選擇的數
狀態數量為 O(n * 2^n * 2^n) = O(n * 2^2n)
轉移時枚舉 n^2 個數字，因此總時間複雜度為 O(n^3 * 2^2n)
"""

from functools import cache

n = int(input())
cube = [[list(map(int, input().split())) for _ in range(n)] for _ in range(n)]

mask = (1 << n) - 1
@cache
def dfs(i, y, z):
    if i == n:
        return 0
    res = float('inf')
    for j in range(n):
        if y & (1 << j): continue
        for k in range(n):
            if z & (1 << k): continue
            res = min(res, cube[i][j][k] + dfs(i + 1, y | (1 << j), z | (1 << k)))
    return res
print(dfs(0, 0, 0))