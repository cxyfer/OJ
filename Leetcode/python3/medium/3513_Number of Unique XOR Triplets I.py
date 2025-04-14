#
# @lc app=leetcode id=3513 lang=python3
#
# [3513] Number of Unique XOR Triplets I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        return n if n < 3 else 1 << n.bit_length()
# @lc code=end

