#
# @lc app=leetcode id=3191 lang=python3
# @lcpr version=30204
#
# [3191] Minimum Operations to Make Binary Array Elements Equal to One I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    Greedy
"""
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        for i in range(n - 2, n): # last 2 elements
            if nums[i] == 0:
                return -1
        return ans
# @lc code=end



#
# @lcpr case=start
# [0,1,1,1,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1]\n
# @lcpr case=end

#

