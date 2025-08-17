#
# @lc app=leetcode id=3653 lang=python3
#
# [3653] XOR After Range Multiplication Queries I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
        return reduce(xor, nums, 0)
# @lc code=end

