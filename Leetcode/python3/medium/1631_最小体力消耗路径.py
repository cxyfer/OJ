#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#
from preImport import *
# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # return self.solve1(heights)
        # return self.solve2(heights)
        return self.solve3(heights)
    """
        1. BFS + Binary Search
    """
    def solve1(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        def check(k): # BFS 檢查當前 mid 是否可到達終點
            DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            q = deque([(0, 0)])
            visited = set([(0, 0)])
            while q:
                x, y = q.popleft()
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        if abs(heights[x][y] - heights[nx][ny]) <= k:
                            q.append((nx, ny))
                            visited.add((nx, ny))
            return (m - 1, n - 1) in visited
        
        left, right = 0, 10**6
        while left <= right: # [left, right]
            mid = (left + right) // 2
            if check(mid): # 可以到達終點，縮小右邊界
                right = mid - 1 
            else:
                left = mid + 1
        return left
    """
        2. Disjoint Set
    """
    def solve2(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = [] # (u, v, w)
        # 對每個點，如果右邊或下面有點，就加入edges
        for i in range(m):
            for j in range(n):
                idx = i * n + j # 為了方便，把每個點編號
                if i + 1 < m:
                    edges.append((idx + n, idx, abs(heights[i + 1][j] - heights[i][j])))
                if j + 1 < n:
                    edges.append((idx + 1, idx, abs(heights[i][j + 1] - heights[i][j])))
        edges.sort(key=lambda x: x[2]) # 按照 weight 排序

        # Disjoint Set
        p = [i for i in range(m * n)]
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[px] = py
        # Kruskal
        st, ed = 0, m * n - 1 # 起點和終點的index
        for u, v, w in edges:
            union(u, v)
            if find(st) == find(ed):
                return w
        return 0 # 起點=終點，返回0
    """
        3. Dijkstra
    """
    def solve3(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)] # dist[i][j] 表示從起點到 (i, j) 的最小體力消耗
        dist[0][0] = 0 
        visited = [[False] * n for _ in range(m)] # 記錄是否已經訪問過

        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = [(0, 0, 0)] # (dist, x, y)
        while q:
            d, x, y = heapq.heappop(q)
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = max(d, abs(heights[x][y] - heights[nx][ny])) # 更新體力消耗
                    if nd < dist[nx][ny]: # 更新 dist
                        dist[nx][ny] = nd
                        heapq.heappush(q, (nd, nx, ny))
        return dist[-1][-1]
# @lc code=end

