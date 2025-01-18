#
# @lc app=leetcode id=452 lang=python3
# @lcpr version=30204
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Greedy
    Activity Selection Problem
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1]) # 依照 x_end 遞增排序
        right = points[0][1] # 貪心，往區間的最右邊射箭
        ans = 1
        for x_st, x_ed in points:
            if x_st > right: # 區間不重疊
                ans += 1
                right = x_ed
        return ans
# @lc code=end



#
# @lcpr case=start
# [[10,16],[2,8],[1,6],[7,12]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4],[5,6],[7,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[4,5]]\n
# @lcpr case=end

#

