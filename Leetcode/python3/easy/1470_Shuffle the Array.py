#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        msk = (1 << 10) - 1
        for i in range(n):
            nums[i << 1] |= (nums[i] & msk) << 10
            nums[(i << 1) | 1] |= (nums[i + n] & msk) << 10
        for i in range(n << 1):
            nums[i] >>= 10
        return nums
# @lc code=end

