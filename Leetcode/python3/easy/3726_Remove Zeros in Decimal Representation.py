#
# @lc app=leetcode id=3726 lang=python3
#
# [3726] Remove Zeros in Decimal Representation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def removeZeros(self, n: int) -> int:
        return int(str(n).replace('0', ''))

class Solution2:
    def removeZeros(self, n: int) -> int:
        ans = 0
        base = 1
        while n > 0:
            n, x = divmod(n, 10)
            if x > 0:
                ans += x * base
                base *= 10
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

