#
# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # return [v == 0 for v in accumulate(nums, lambda x, y: ((x << 1) + y) % 5)]
        ans = []
        v = 0
        for b in nums:
            v = ((v << 1) + b) % 5
            ans.append(v == 0)
        return ans
# @lc code=end

