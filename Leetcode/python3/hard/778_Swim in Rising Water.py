#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Disjoint Set
2. Binary Search + DFS / BFS
3. Dijkstra
"""
# @lc code=start
class Solution1:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # DSU
        pa = list(range(n * n))
        def find(x) -> int:
            while pa[x] != x:
                pa[x] = pa[pa[x]]
                x = pa[x]
            return x
        def union(x, y) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            pa[fy] = fx
            return True

        # Kruskal
        edges = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i < n - 1:
                    edges.append((i * n + j, (i + 1) * n + j, max(x, grid[i + 1][j])))
                if j < n - 1:
                    edges.append((i * n + j, i * n + j + 1, max(x, grid[i][j + 1])))
        edges.sort(key=lambda x: x[2])

        for u, v, w in edges:
            union(u, v)
            if find(0) == find(n * n - 1):
                return w
        return 0

class Solution2:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def check(k):
            vis = set([(0, 0)])
            def dfs(x, y):
                if x == n - 1 and y == n - 1:
                    return True
                for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in vis and grid[nx][ny] <= k:
                        vis.add((nx, ny))
                        if dfs(nx, ny):
                            return True
                return False
            return dfs(0, 0)

        left, right = max(grid[0][0], grid[n - 1][n - 1]), n * n - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

class Solution3:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        hp = [(dist[0][0], 0, 0)]  # (dist, x, y)
        while hp:
            d, x, y = heappop(hp)
            if d > dist[x][y]:
                continue
            for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= nx < n and 0 <= ny < n:
                    nd = max(d, grid[nx][ny])
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heappush(hp, (nd, nx, ny))
        return dist[-1][-1]

# Solution = Solution1
Solution = Solution2
# Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.swimInWater([[3,2],[0,1]]))  # 3