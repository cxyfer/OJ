#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Offline Query + Kruskal's Algorithm
  - 由於是網格圖，因此事前連邊時，只連右和下即可
  - 這種寫法支援查詢時從任何一格開始，且也能改變判斷條件，例如改成當兩格之和 <= v 時連邊等
2. Offline Query + Heap
  - 由於起點是 (0, 0)，且邊的 weight 是兩格的 max value，所以可以維護未訪問點的 value 即可
"""
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
    
class Solution1:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        edges = []
        for qi, row in enumerate(grid):
            for j, v in enumerate(row):
                # 相連的 cost 為兩格的 max value，且由於會重複，只需向右下兩個方向邊即可
                for x, y in [(qi + 1, j), (qi, j + 1)]:  
                    if x >= m or y >= n:
                        continue
                    edges.append((max(v, grid[x][y]), qi * n + j, x * n + y))  
        edges.sort()

        ans = [0] * len(queries)
        idx = 0
        for qi, v in sorted(enumerate(queries), key=lambda x: x[1]):
            while idx < len(edges) and edges[idx][0] < v:
                _, x, y = edges[idx]
                idx += 1
                uf.union(x, y)
            ans[qi] = uf.sz[uf.find(0)] if grid[0][0] < v else 0
        return ans
    
class Solution2:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        hp = [(grid[0][0], 0, 0)]
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True

        ans = [0] * len(queries)
        cnt = 0
        for qi, v in sorted(enumerate(queries), key=lambda x: x[1]):
            while hp and hp[0][0] < v:
                _, x, y = heappop(hp)
                vis[x][y] = True
                cnt += 1
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or vis[nx][ny]:
                        continue
                    vis[nx][ny] = True
                    heappush(hp, (grid[nx][ny], nx, ny))
            ans[qi] = cnt
        return ans

Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2]))  # [5,8,1]
print(sol.maxPoints([[5,2,1],[1,1,2]], [3]))  # [0]
