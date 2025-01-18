#
# @lc app=leetcode id=3033 lang=python3
# @lcpr version=30204
#
# [3033] Modify the Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        mx = [max([matrix[i][j] for i in range(m)]) for j in range(n)]
        return [[matrix[i][j] if matrix[i][j] != -1 else mx[j] for j in range(n)] for i in range(m)]
# @lc code=end



#
# @lcpr case=start
# [[1,2,-1],[4,-1,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,-1],[5,2]]\n
# @lcpr case=end

#

