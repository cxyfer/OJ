# @algorithm @lc id=3330 lang=python3 
# @title modify-the-matrix


from en.Python3.mod.preImport import *
# @test([[1,2,-1],[4,-1,6],[7,8,9]])=[[1,2,9],[4,8,6],[7,8,9]]
# @test([[3,-1],[5,2]])=[[3,2],[5,2]]
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        mx = [max([matrix[i][j] for i in range(m)]) for j in range(n)]
        ans = [[matrix[i][j] if matrix[i][j] != -1 else mx[j] for j in range(n)] for i in range(m)]
        return ans