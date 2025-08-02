#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0] * i for i in range(1, numRows + 1)]
        for i in range(numRows):
            ans[i][0] = ans[i][-1] = 1
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans
# @lc code=end

