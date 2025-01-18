# @algorithm @lc id=1677 lang=python3 
# @title matrix-diagonal-sum


from en.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=25
# @test([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])=8
# @test([[5]])=5
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        left, right = 0, n-1
        for i in range(n):
            ans += mat[i][left] + mat[i][right]
            left += 1
            right -= 1
        if n % 2 == 1:
            ans -= mat[n//2][n//2]
        return ans
        