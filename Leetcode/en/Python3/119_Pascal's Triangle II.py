# @algorithm @lc id=119 lang=python3 
# @title pascals-triangle-ii


from en.Python3.mod.preImport import *
# @test(3)=[1,3,3,1]
# @test(0)=[1]
# @test(1)=[1,1]
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            ans = [1] + [ans[i] + ans[i+1] for i in range(len(ans)-1)] + [1]
        return ans