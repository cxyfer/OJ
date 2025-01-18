#
# @lc app=leetcode id=885 lang=python3
# @lcpr version=30204
#
# [885] Spiral Matrix III
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [(rStart, cStart)]
        if rows * cols == 1: return ans
        r, c = rStart, cStart
        for k in range(1, 2*(rows+cols), 2):
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):
                for _ in range(dk):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append((r, c))
                        if len(ans) == rows * cols:
                            return ans
        return ans
# @lc code=end



#
# @lcpr case=start
# 1\n4\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# 5\n6\n1\n4\n
# @lcpr case=end

#

