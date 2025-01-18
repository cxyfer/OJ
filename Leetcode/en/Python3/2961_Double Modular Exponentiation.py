# @algorithm @lc id=3234 lang=python3 
# @title double-modular-exponentiation


from en.Python3.mod.preImport import *
# @test([[2,3,3,10],[3,3,3,1],[6,1,1,4]],2)=[0,2]
# @test([[39,3,1000,1000]],17)=[]
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            if pow(pow(a, b, 10), c, m) == target:
                ans.append(i)
        return ans