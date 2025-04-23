#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Recursive
"""
# @lc code=start
class Solution1:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = self.grayCode(n - 1)
        return res + [x | (1 << (n - 1)) for x in reversed(res)]
    
class Solution2:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(n):
            ans += [x | (1 << i) for x in reversed(ans)]
        return ans

Solution = Solution1
# Solution = Solution2
# @lc code=end

