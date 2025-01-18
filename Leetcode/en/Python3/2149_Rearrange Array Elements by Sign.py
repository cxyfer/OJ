# @algorithm @lc id=2271 lang=python3 
# @title rearrange-array-elements-by-sign


from en.Python3.mod.preImport import *
# @test([3,1,-2,-5,2,-4])=[3,-2,1,-5,2,-4]
# @test([-1,1])=[1,-1]
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pos, neg = 0, 0 # Two pointers
        for i in range(n//2):
            while pos < n and nums[pos] < 0:
                pos += 1
            while neg < n and nums[neg] > 0:
                neg += 1
            ans[i*2] = nums[pos]
            ans[i*2+1] = nums[neg]
            pos += 1
            neg += 1
        return ans