# @algorithm @lc id=2866 lang=python3 
# @title longest-even-odd-subarray-with-threshold


from en.Python3.mod.preImport import *
# @test([3,2,5,4],5)=3
# @test([1,2],2)=1
# @test([2,3,4,5],4)=3
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        i = 0
        while (i < n):
            if nums[i] > threshold or nums[i] % 2 != 0:
                i += 1 
                continue
            st = i # left
            i += 1 # right
            while i < n and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                i += 1
            ans = max(ans, i - st)
        return ans