#
# @lc app=leetcode.cn id=2413 lang=python3
#
# [2413] 最小偶倍数
#

# @lc code=start
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2

# @lc code=end

