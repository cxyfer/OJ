# @algorithm @lc id=3372 lang=python3 
# @title longest-strictly-increasing-or-strictly-decreasing-subarray


from en.Python3.mod.preImport import *
# @test([1,4,3,3,2])=2
# @test([3,3,3,3])=1
# @test([3,2,1])=3
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        return self.solve2(nums)
    """
        1. Brute force
        Time: O(n^2)
    """
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        for i in range(n): 
            for j in range(i+1, n):
                if nums[j] <= nums[j-1]: # strictly increasing
                    break
                ans = max(ans, j-i+1)
            for j in range(i+1, n):
                if nums[j] >= nums[j-1]: # strictly decreasing
                    break
                ans = max(ans, j-i+1)
        return ans
    """
        2. 分組循環
        Time: O(n)
    """
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        i = 0
        while i < n - 1: # 分組循環
            if nums[i] == nums[i + 1]:
                i += 1
                continue
            st = i # 記錄當前分組的起始位置
            is_inc = nums[i] < nums[i + 1] # 判斷是遞增還是遞減
            i += 2 # nums[i] 和 nums[i+1] 已經判斷過了
            while i < n and nums[i] != nums[i - 1] and (nums[i] > nums[i - 1]) == is_inc: 
                i += 1
            ans = max(ans, i - st) # [st, i-1] 是嚴格遞增或遞減的子陣列
            i -= 1 # 從 i-1 開始下一輪
        return ans