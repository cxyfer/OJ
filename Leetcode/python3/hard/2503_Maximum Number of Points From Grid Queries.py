#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
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
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        edges = []
        for qi, row in enumerate(grid):
            for j, v in enumerate(row):
                for x, y in [(qi + 1, j), (qi, j + 1)]:  # 只需跟右和下連邊即可
                    if x >= m or y >= n:
                        continue
                    edges.append((max(v, grid[x][y]), qi * n + j, x * n + y))
        edges.sort()
        queries = [(v, qi) for qi, v in enumerate(queries)]
        queries.sort()
        ans = [0] * len(queries)
        idx = 0
        for v, qi in queries:
            while idx < len(edges) and edges[idx][0] < v:
                _, x, y = edges[idx]
                idx += 1
                uf.union(x, y)
            ans[qi] = uf.sz[uf.find(0)] if grid[0][0] < v else 0
        return ans
# @lc code=end

sol = Solution()
print(sol.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]))  # [5,8,1]
print(sol.maxPoints([[5,2,1],[1,1,2]], [3]))  # [0]
