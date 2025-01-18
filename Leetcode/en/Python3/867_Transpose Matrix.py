# @algorithm @lc id=898 lang=python3 
# @title transpose-matrix


from en.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=[[1,4,7],[2,5,8],[3,6,9]]
# @test([[1,2,3],[4,5,6]])=[[1,4],[2,5],[3,6]]
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [ [0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = matrix[j][i]
        return ans