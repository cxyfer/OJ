#
# @lc app=leetcode id=3806 lang=python3
#
# [3806] Maximum Bitwise AND After Increment Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
試填法
原題: https://atcoder.jp/contests/arc146/tasks/arc146_b
"""
# @lc code=start
class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        B = (max(nums) + k).bit_length()
        ans = 0
        for b in range(B, -1, -1):
            tgt = ans | (1 << b)
            def cost(x):
                if (x & tgt) == tgt:
                    return 0
                else:
                    msb = (tgt & ~x).bit_length() - 1
                    y = ((x >> msb) + 1) << msb
                    y |= (tgt & ((1 << msb) - 1))
                    return y - x
            if sum(sorted(cost(x) for x in nums)[:m]) <= k:
                ans |= (1 << b)
        return ans
# @lc code=end

