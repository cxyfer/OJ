#
# @lc app=leetcode id=3402 lang=python3
# @lcpr version=30204
#
# [3402] Minimum Operations to Make Columns Strictly Increasing
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        for col in zip(*grid):
            prev = -float('inf')
            for x in col:
                # if x > prev:
                #     prev = x
                # else:
                #     ans += (prev + 1) - x
                #     prev = prev + 1
                ans += max(prev + 1 - x, 0)
                prev = max(prev + 1, x)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[3,2],[1,3],[3,4],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,2,1],[2,1,0],[1,2,3]]\n
# @lcpr case=end

#

