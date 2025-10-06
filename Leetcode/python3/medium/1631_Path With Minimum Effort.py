#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Disjoint Set
2. Binary Search + DFS / BFS
3. Dijkstra

Similar to 778. Swim in Rising Water
"""
# @lc code=start
max = lambda a, b: a if a > b else b

class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])

        # DSU
        pa = list(range(n * m))
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
        for i, row in enumerate(heights):
            for j, x in enumerate(row):
                if i < n - 1:
                    edges.append((i * m + j, (i + 1) * m + j, abs(x - heights[i + 1][j])))
                if j < m - 1:
                    edges.append((i * m + j, i * m + (j + 1), abs(x - heights[i][j + 1])))
        edges.sort(key=lambda x: x[2])

        for u, v, w in edges:
            union(u, v)
            if find(0) == find(n * m - 1):
                return w
        return 0

class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])

        def check(k):
            vis = set([(0, 0)])
            def dfs(x, y):
                if x == n - 1 and y == m - 1:
                    return True
                for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vis and abs(heights[x][y] - heights[nx][ny]) <= k:
                        vis.add((nx, ny))
                        if dfs(nx, ny):
                            return True
                return False
            return dfs(0, 0)

        left, right = 0, int(1e6) - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

class Solution3:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        hp = [(0, 0, 0)]  # (dist, x, y)
        while hp:
            d, x, y = heappop(hp)
            if d > dist[x][y]:
                continue
            for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= nx < n and 0 <= ny < m:
                    nd = max(d, abs(heights[x][y] - heights[nx][ny]))
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        heappush(hp, (nd, nx, ny))
        return dist[-1][-1]

Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# @lc code=end

