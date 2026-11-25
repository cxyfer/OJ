#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # return sum(len(row) - bisect_right(row, 0, key = lambda x: -x) for row in grid)
        ans = 0
        for row in grid:
            idx = bisect_right(row, 0, key=lambda x: -x)
            ans += len(row) - idx
        return ans


class Solution2:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Follow-up: O(n + m) 的階梯走法
        # 利用每行和每列都是從左到右、從上到下非遞增的特性。

        n, m = len(grid), len(grid[0])
        i, j = n - 1, 0
        ans = 0
        while i >= 0 and j < m:
            if grid[i][j] < 0:  # 此橫列(row)從 j 開始往右都是負數
                ans += m - j
                i -= 1
            else:  # 此直行(column)從 i 開始往上都不會是負數
                j += 1
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

