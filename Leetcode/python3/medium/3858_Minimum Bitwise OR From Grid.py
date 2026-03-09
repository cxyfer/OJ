#
# @lc app=leetcode id=3858 lang=python3
#
# [3858] Minimum Bitwise OR From Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        B = max(map(max, grid)).bit_length()
        ans = 0
        # 判斷 ans 的第 b 位是否可以為 0
        for b in range(B - 1, -1, -1):
            for row in grid:
                for x in row:
                    if ((x | ans) >> b) << b == ans:
                        break
                else:
                    # 在高位的限制下，第 b 位只能為 1
                    ans |= (1 << b)
                    break
        return ans
# @lc code=end

