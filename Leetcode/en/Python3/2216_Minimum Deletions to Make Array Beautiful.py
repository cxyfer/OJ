# @algorithm @lc id=1355 lang=python3 
# @title minimum-deletions-to-make-array-beautiful


from en.Python3.mod.preImport import *
# @test([1,1,2,3,5])=1
# @test([1,1,2,2,3,3])=2
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if (i-ans) % 2 == 0 and i + 1 < n: # 最終的下標為i-ans，枚舉最終的偶數下標
                if nums[i] == nums[i+1]: # 連續兩個數字相同，刪去其一
                    ans += 1
        return ans if (n - ans) % 2 == 0 else ans+1 