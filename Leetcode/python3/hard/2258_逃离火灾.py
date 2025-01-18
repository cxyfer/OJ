#
# @lc app=leetcode.cn id=2258 lang=python3
#
# [2258] 逃离火灾
#
from preImport import *
# @lc code=start
class Solution:
    """
        BFS + Binary Search
    """
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def check(t: int) -> bool: # 是否能在初始位置停留 t 分鐘
            fires = [(i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == 1] 
            on_fire = set(fires) # 著火的位置
            def spread_fire(): # 火的 BFS
                nonlocal fires
                tmp = fires
                fires = []
                for i, j in tmp:
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in on_fire:
                            on_fire.add((x, y))  # 标记着火的位置
                            fires.append((x, y))
            while t and fires: # 在 t 分鐘內，讓火擴散 (BFS)
                spread_fire() # 火擴散 (BFS)
                t -= 1
            if (0, 0) in on_fire: # 起點著火
                return False

            # 人的 BFS
            q = [(0, 0)]
            visited = set(q)
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    if (i, j) in on_fire: continue # 人被火燒到
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 上下左右
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and (x, y) not in on_fire and (x, y) not in visited:
                            if x == m - 1 and y == n - 1: # 到達安全屋
                                return True
                            visited.add((x, y)) # 避免重複走到同一個位置
                            q.append((x, y))
                spread_fire() # 火擴散
            return False # 人被火燒到，或者人走不到安全屋

        left = 0
        right = m * n
        while left <= right: # [left, right]
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right if right != m * n else 10 ** 9
# @lc code=end

