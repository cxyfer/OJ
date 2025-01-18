#
# @lc app=leetcode id=2595 lang=python3
# @lcpr version=30204
#
# [2595] Number of Even and Odd Bits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        idx = 0
        while n:
            ans[idx] += n & 1
            idx ^= 1
            n >>= 1
        return ans

class Solution2:
    def evenOddBit(self, n: int) -> List[int]:
        mask = 0xAAAAAAAA
        return [(n & (mask >> 1)).bit_count(), (n & mask).bit_count()]

class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# 50\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

