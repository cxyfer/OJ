# @algorithm @lc id=3165 lang=python3 
# @title find-indices-with-index-and-value-difference-i


from en.Python3.mod.preImport import *
# @test([5,1,4,1],2,4)=[0,3]
# @test([2,1],0,0)=[0,0]
# @test([1,2,3],2,4)=[-1,-1]
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(i-j) >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    return [i,j]
        return [-1,-1]