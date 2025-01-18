# @algorithm @lc id=1704 lang=python3 
# @title special-positions-in-a-binary-matrix


from en.Python3.mod.preImport import *
# @test([[1,0,0],[0,0,1],[1,0,0]])=1
# @test([[1,0,0],[0,1,0],[0,0,1]])=3
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                row[i] += mat[i][j]
                col[j] += mat[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ans += 1
        return ans