#
# @lc app=leetcode id=624 lang=python3
# @lcpr version=30204
#
# [624] Maximum Distance in Arrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        mn, mx = arrays[0][0], arrays[0][-1]
        ans = -float("inf")
        for i in range(1, n):
            a, b = arrays[i][0], arrays[i][-1]
            ans = max(ans, mx - a, b - mn)
            mn, mx = min(mn, a), max(mx, b)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5],[1,2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[1]]\n
# @lcpr case=end

#

