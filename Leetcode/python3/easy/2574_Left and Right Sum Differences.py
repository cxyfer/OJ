#
# @lc app=leetcode id=2574 lang=python3
#
# [2574] Left and Right Sum Differences
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre = 0
        suf = sum(nums)

        ans = []
        for x in nums:
            suf -= x
            ans.append(abs(pre - suf))
            pre += x
        return ans
# @lc code=end

