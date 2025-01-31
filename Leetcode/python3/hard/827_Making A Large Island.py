#
# @lc app=leetcode id=827 lang=python3
# @lcpr version=30204
#
# [827] Making A Large Island
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class UnionFind:
    __slots__ = ['n', 'pa', 'sz', 'cnt']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點
        self.sz = [1] * n # 連通分量大小
        self.cnt = n # 連通分量數量

    def find(self, x: int) -> int:
        while self.pa[x] != x:
            self.pa[x] = self.pa[self.pa[x]]
            x = self.pa[x]
        return x

    def union(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.sz[fx] < self.sz[fy]:
            fx, fy = fy, fx
        self.pa[fy] = fx
        self.sz[fx] += self.sz[fy]
        self.cnt -= 1
        return True

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == 0:
                    continue
                for dx, dy in [(1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        uf.union(x * n + y, nx * n + ny)
        ans = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == 1:
                    continue
                cur = 1
                vis = set()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (u := uf.find(nx * n + ny)) not in vis:
                        vis.add(u)
                        cur += uf.sz[u]
                ans = max(ans, cur)
        return n * n if ans == 0 else ans
# @lc code=end

sol = Solution()
print(sol.largestIsland([[1,0],[0,1]]))
print(sol.largestIsland([[1,1],[1,0]]))
print(sol.largestIsland([[1,1],[1,1]]))

# @lcpr case=start
# [[1,0],[0,1]]\n
# @lcpr case=end




# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1]]\n
# @lcpr case=end

#

