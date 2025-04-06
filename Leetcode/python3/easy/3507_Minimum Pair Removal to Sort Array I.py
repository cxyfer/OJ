3#
# @lc app=leetcode id=3507 lang=python3
#
# [3507] Minimum Pair Removal to Sort Array I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while not sorted(nums) == nums:
            mn = (float('inf'), -1)
            for i, (x, y) in enumerate(pairwise(nums)):
                mn = min(mn, (x + y, i))
            nums[mn[1]] = mn[0]
            nums.pop(mn[1] + 1)
            ans += 1
        return ans
# @lc code=end

