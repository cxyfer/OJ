from functools import cache

import sys
buf = sys.stdin.read().split()
cin = lambda: buf.pop(0)

while True:
    try:
        n, m = int(cin()), int(cin())
    except IndexError:
        break
    grid = [[int(cin()) for _ in range(m)] for _ in range(n)]

    next = [[-1] * m for _ in range(n)] # 紀錄路徑
    # dfs(i, j) 表示從 (i, j) 到終點的最短路徑
    @cache
    def dfs(i, j):
        if j == m - 1:
            return grid[i][j]
        res = float('inf')
        for di in [-1, 0, 1]:
            ni = (i + di) % n
            nd = dfs(ni, j + 1) + grid[i][j]
            if nd < res or (nd == res and ni < next[i][j]):
                res = nd
                next[i][j] = ni
        return res

    ans = dfs(0, 0)
    i = 0
    for j in range(m):
        print(i + 1, end=' ' if j < m - 1 else '\n')
        i = next[i][j]
    print(ans)