#
# @lc app=leetcode.cn id=1329 lang=python3
#
# [1329] 将矩阵按对角线排序
#
from preImport import *
# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        diag = [[] for _ in range(n + m)]
        for i in range(n):
            for j in range(m):
                diag[i - j + m].append(mat[i][j])
        for d in diag:
            d.sort(reverse=True)
        for i in range(n):
            for j in range(m):
                mat[i][j] = diag[i - j + m].pop()
        return mat
# @lc code=end
sol = Solution()
print(sol.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
print(sol.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))