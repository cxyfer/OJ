# @algorithm @lc id=2870 lang=python3 
# @title longest-alternating-subarray


from en.Python3.mod.preImport import *
# @test([2,3,4,3,4])=4
# @test([4,5,6])=2
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        seen = set() # 用來記錄可以做為起點的下標
        for i in range(n):
            if i in seen:
                continue
            seen.add(i)
            cur = 1
            sign = 1
            for j in range(i+1, n):
                if nums[j] - nums[j-1] == sign:
                    cur += 1
                    sign *= -1
                    if sign == 1:
                        seen.add(j)
                else:
                    break
            if cur > 1: # 長度至少為 2
                ans = max(ans, cur)
        return ans