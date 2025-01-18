# @algorithm @lc id=1580 lang=python3 
# @title shuffle-the-array


from en.Python3.mod.preImport import *
# @test([2,5,1,3,4,7],3)=[2,3,5,4,1,7]
# @test([1,2,3,4,4,3,2,1],4)=[1,4,2,3,3,2,4,1]
# @test([1,1,2,2],2)=[1,2,1,2]
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans