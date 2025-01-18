from functools import cache

MOD = 1000007
t = int(input())

for kase in range(1, t+1):
    n = int(input())
    grid = []
    B = set()
    for i in range(n):
        grid.append(list(input()))
        for j in range(n):
            if grid[i][j] == 'W':
                x, y = i, j
            elif grid[i][j] == 'B':
                B.add((i, j))

    @cache
    def dfs(i, j):
        if i == 0 and 0 <= j < n:
            return 1
        if i < 0 or i >= n or j < 0 or j >= n:
            return 0
        res = 0
        for dx, dy in [(-1, -1), (-1, 1)]:
            if (i+dx, j+dy) not in B:
                res += dfs(i+dx, j+dy)
            elif (i+2*dx, j+2*dy) not in B:
                res += dfs(i+2*dx, j+2*dy)
        return res
    
    print("Case %d: " % kase, end="")
    print(dfs(x, y) % MOD)