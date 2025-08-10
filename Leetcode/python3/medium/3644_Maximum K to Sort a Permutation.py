#
# @lc app=leetcode id=3644 lang=python3
#
# [3644] Maximum K to Sort a Permutation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = reduce(and_, [i for i, x in enumerate(nums) if x != i], -1)
        return ans if ans != -1 else 0
# @lc code=end

