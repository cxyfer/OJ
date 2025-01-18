# @algorithm @lc id=118 lang=python3 
# @title pascals-triangle


from en.Python3.mod.preImport import *
# @test(5)=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# @test(1)=[[1]]
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0]*i for i in range(1,numRows+1)]
        ans[0][0] = 1
        for i in range(1, numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
        return ans