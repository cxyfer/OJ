# @algorithm @lc id=3241 lang=python3 
# @title divide-array-into-arrays-with-max-difference


from en.Python3.mod.preImport import *
# @test([1,3,4,8,7,9,3,5,1],2)=[[1,1,3],[3,4,5],[7,8,9]]
# @test([1,3,3,2,7,3],3)=[]
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = [nums[i*3:i*3+3] for i in range(n // 3)]
        for row in ans:
            if row[2] - row[0] > k:
                return []
        return ans