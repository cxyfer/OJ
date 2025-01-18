#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直区域
#
from preImport import *
# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x: x[0])
        ans = 0
        for i in range(1, n):
            ans = max(ans, points[i][0] - points[i - 1][0])
        return ans
# @lc code=end
sol = Solution()
print(sol.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])) # 1
print(sol.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])) # 3