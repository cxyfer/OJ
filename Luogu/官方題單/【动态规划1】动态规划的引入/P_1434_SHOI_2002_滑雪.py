"""
P1434 [SHOI2002] 滑雪
https://www.luogu.com.cn/problem/P1434
網格圖上的 DAG DP / 記憶化搜索
"""

import sys
from functools import cache

sys.setrecursionlimit(int(1e4 + 5))


def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    @cache
    def dfs(x, y):
        res = 0
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] < grid[x][y]:
                res = max(res, dfs(nx, ny))
        return res + 1

    print(max(dfs(x, y) for x in range(n) for y in range(m)))


if __name__ == "__main__":
    solve()
