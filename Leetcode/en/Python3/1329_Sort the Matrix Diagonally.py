# @algorithm @lc id=1253 lang=python3 
# @title sort-the-matrix-diagonally


from en.Python3.mod.preImport import *
# @test([[3,3,1,1],[2,2,1,2],[1,1,1,2]])=[[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# @test([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]])=[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
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