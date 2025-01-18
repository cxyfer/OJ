#
# @lc app=leetcode id=2708 lang=python3
# @lcpr version=30204
#
# [2708] Maximum Strength of a Group
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        mx = mn = nums[0]
        for i in range(1, n):
            x = nums[i]
            new_mx = max(mx, x, mx * x, mn * x)
            new_mn = min(mn, x, mx * x, mn * x)
            mx, mn = new_mx, new_mn
        return mx
# @lc code=end



#
# @lcpr case=start
# [3,-1,-5,2,5,-9]\n
# @lcpr case=end

# @lcpr case=start
# [-4,-5,-4]\n
# @lcpr case=end

#

