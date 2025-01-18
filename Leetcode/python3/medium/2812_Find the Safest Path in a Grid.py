#
# @lc app=leetcode id=2812 lang=python3
# @lcpr version=30202
#
# [2812] Find the Safest Path in a Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. 多源BFS + DFS/BFS/DSU + Binary Search
            首先用多源BFS計算每個點到最近的 1 的曼哈頓距離，因此問題可以轉換成，是否存在一條從起點到終點的路徑，使得每個點到最近的 1 的距離都 >= x。
            而最大化最小值，可以想到二分答案，對於每個 x ，檢查是否存在這樣的路徑。
        2. 多源BFS + DSU
            在 1. 預處理到最近的 1 的曼哈頓距離的基礎上優化，可以從最大距離開始枚舉距離 x ，將所有距離 >= x 的點合併，
            若起點和終點在同一個集合中，則存在一條路徑，使得每個點到最近的 1 的距離都 >= x。
            由於每個點只會被合併一次，因此若將DSU的時間複雜度視為 O(1) ，則時間複雜度約為 O(n^2) 。
    """
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        return self.solve1(grid)
        # return self.solve2(grid)
    def solve1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 多源BFS計算每個點到最近的 1 的曼哈頓距離
        dist = [[-1] * n for _ in range(n)] 
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j, 0))
        while q:
            i, j, d = q.popleft()
            for nx, ny in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = d + 1
                    q.append((nx, ny, d+1))
        # 對答案二分，這裡使用BFS來檢查是否存在一條路徑
        def check(x):
            if dist[0][0] < x:
                return False
            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visited[0][0] = True
            while q:
                i, j = q.popleft()
                if i == n-1 and j == n-1:
                    return True
                for nx, ny in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= x:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return False
        left, right = 0, 2*n-2 # [0, 2n-2]
        while left <= right: # 區間不為空
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
    def solve2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 多源BFS計算每個點到最近的 1 的曼哈頓距離
        dist = [[-1] * n for _ in range(n)] 
        q = deque()
        groups = defaultdict(list) # 保存距離到點的對應關係
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j, 0))
                    groups[0].append((i, j))
        while q:
            i, j, d = q.popleft()
            for nx, ny in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = d + 1
                    q.append((nx, ny, d+1))
                    groups[d+1].append((nx, ny))
        # DSU
        fa = [i for i in range(n*n)] # 將二維座標轉換為一維
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                fa[x] = y
        # 從最大距離開始枚舉 x
        for d in range(max(groups.keys()), 0, -1):
            for i, j in groups[d]:
                for nx, ny in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] >= d: # 周圍有距離 >= x 的點，則使其連通
                        union(i*n+j, nx*n+ny)
                if find(0) == find(n*n-1): # 起點和終點在同一個集合中
                    return d
        return 0
# @lc code=end

sol = Solution()
print(sol.maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]])) # 0
print(sol.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]])) # 2
print(sol.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])) # 2

#
# @lcpr case=start
# [[1,0,0],[0,0,0],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,1],[0,0,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]\n
# @lcpr case=end

#

