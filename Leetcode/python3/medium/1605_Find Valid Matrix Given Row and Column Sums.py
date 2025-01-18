#
# @lc app=leetcode id=1605 lang=python3
# @lcpr version=30204
#
# [1605] Find Valid Matrix Given Row and Column Sums
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        matrix = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            v = min(rowSum[i], colSum[j])
            matrix[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        return matrix
# @lc code=end



#
# @lcpr case=start
# [3,8]\n[4,7]\n
# @lcpr case=end

# @lcpr case=start
# [5,7,10]\n[8,6,8]\n
# @lcpr case=end

#

