#
# @lc app=leetcode id=48 lang=python3
# @lcpr version=30201
#
# [48] Rotate Image
#


# @lcpr-template-start
from preImport import *


# @lcpr-template-end
# @lc code=start
class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                (
                    matrix[i][j],
                    matrix[n - 1 - j][i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[j][n - 1 - i],
                ) = (
                    matrix[n - 1 - j][i],
                    matrix[n - 1 - i][n - 1 - j],
                    matrix[j][n - 1 - i],
                    matrix[i][j],
                )

class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reflect
        for i in range(n):
            matrix[i].reverse()


Solution = Solution1
# Solution = Solution2
# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#
