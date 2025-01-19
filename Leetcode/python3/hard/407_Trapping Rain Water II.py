#
# @lc app=leetcode id=407 lang=python3
# @lcpr version=30204
#
# [407] Trapping Rain Water II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        hp = []
        vis = [[False] * n for _ in range(m)]
        for i, row in enumerate(heightMap):
            for j, h in enumerate(row):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    hp.append((h, i, j))
                    vis[i][j] = True
        heapify(hp)
        ans = 0
        while hp:
            h, i, j = heappop(hp)
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and not vis[x][y]:
                    ans += max(h - heightMap[x][y], 0)
                    heappush(hp, (max(h, heightMap[x][y]), x, y))
                    vis[x][y] = True
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]\n
# @lcpr case=end

#

