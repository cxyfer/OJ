# @algorithm @lc id=3221 lang=python3 
# @title find-the-peaks


from en.Python3.mod.preImport import *
# @test([2,4,4])=[]
# @test([1,4,3,8,5])=[1,3]
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        ans = []
        for i in range(1, n-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                ans.append(i)
        return ans