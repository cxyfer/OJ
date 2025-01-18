#
# @lc app=leetcode.cn id=1611 lang=python3
#
# [1611] 使整数变为 0 的最少操作次数
#

# @lc code=start
class Solution:
    """
        Gray code
    """
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans ^= n
            n >>= 1
        return ans
# @lc code=end

