# @algorithm @lc id=1586 lang=python3 
# @title longest-subarray-of-1s-after-deleting-one-element


from en.Python3.mod.preImport import *
# @test([1,1,0,1])=3
# @test([0,1,1,1,0,1,1,0,1])=5
# @test([1,1,1])=2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        ans = p1 = p2 = 0
        while idx < n:
            if nums[idx] == 1:
                p2 += 1
            else:
                p1 = p2
                p2 = 0
            idx += 1
            ans = max(ans, p1+p2)
        return ans-1 if ans == n else ans