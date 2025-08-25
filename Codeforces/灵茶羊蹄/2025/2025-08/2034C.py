"""
2034C. Trapped in the Witch's Labyrinth

靈神題解：
什么情况下，无法离开网格图？
1. 当前格子在环中。
2. 当前格子可以到达环。
3. 我们从一个格子移动到了问号格子。把这个问号格子改成反方向，就可以来回横跳了，无法离开网格图。

考虑子问题：
1. 如果起点不是问号，那么问题变成：把下一步的那个格子当作起点，能否离开网格图？这是一个子问题。
2. 如果起点是问号，那么上下左右要有无法离开网格图的格子；或者上下左右有问号，把起点及其邻居这两个问号改成相向的，就可以来回横跳了。

考虑用记忆化搜索 dfs(i,j) 实现：
1. 如果出界，返回 0。
2. 如果之前计算过，返回之前计算的值。
3. 首先，把 memo[i][j] 标记为 1，暂定这个格子是无法走出去的。这样可以避免 dfs 遇到环导致无限递归。
4. 如果当前格子不是问号，那么继续递归 dfs(x,y)。
5. 否则，看看上下左右有没有问号，或者无法走出去的格子。如果有，返回 1。
6. 否则返回 0。

答案为所有 dfs(i,j) 之和。
"""

import sys
sys.setrecursionlimit(int(1e5))

def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    memo = [[-1] * m for _ in range(n)]
    def dfs(i: int, j: int) -> int:
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        memo[i][j] = 1
        if grid[i][j] == 'U':
            memo[i][j] = dfs(i - 1, j)
        elif grid[i][j] == 'D':
            memo[i][j] = dfs(i + 1, j)
        elif grid[i][j] == 'L':
            memo[i][j] = dfs(i, j - 1)
        elif grid[i][j] == 'R':
            memo[i][j] = dfs(i, j + 1)
        else:
            memo[i][j] = dfs(i - 1, j) or dfs(i + 1, j) or dfs(i, j - 1) or dfs(i, j + 1)
        return memo[i][j]
        
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += dfs(i, j)
    print(ans)

t = int(input())
for _ in range(t):
    solve()