#
# @lc app=leetcode.cn id=2444 lang=python3
#
# [2444] 统计定界子数组的数目
#
from preImport import *
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # return self.solve1(nums, minK, maxK)
        return self.solve2(nums, minK, maxK)
    """
        1. 分組循環 + Sliding Window 
    """
    def solve1(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        groups = []
        i = 0
        while i < n: # 分組，使每組的數字都在[minK, maxK]之間
            while i < n and not minK <= nums[i] <= maxK: # 找到第一個符合條件的數字
                i += 1
            if i == n:
                break
            st = i
            while i + 1 < n and minK <= nums[i+1] <= maxK:
                i += 1
            groups.append((st, i))
            i += 1
        ans = 0
        for L, R in groups:
            min_idx = max_idx = -1
            for right in range(L, R+1): # 枚舉窗口的右端點
                if nums[right] == minK:
                    min_idx = right
                if nums[right] == maxK:
                    max_idx = right
                left = min(min_idx, max_idx) # 窗口需包含minK和maxK，故窗口的左端點為min(min_idx, max_idx)
                if left != -1: # 窗口的左端點存在
                    ans += left - L + 1
        return ans
    """
        2. 一次遍歷的簡潔寫法，在遍歷時維護每組的左界
        修改自靈神的題解：
        https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/solutions/1895713/jian-ji-xie-fa-pythonjavacgo-by-endlessc-gag2/
    """
    def solve2(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_idx, max_idx, L = -1, -1, 0
        for i, x in enumerate(nums):
            if x == minK:
                min_idx = i
            if x == maxK:
                max_idx = i
            if not minK <= x <= maxK: # 子陣列不能包含 nums[L-1]
                L = i + 1
            left = min(min_idx, max_idx)
            if left >= L:
                ans += left - L + 1
        return ans
# @lc code=end
# @test([1,3,5,2,7,5],1,5)=2
# @test([1,1,1,1],1,1)=10
print(Solution().countSubarrays([1,3,5,2,7,5],1,5)) # 2
print(Solution().countSubarrays([1,1,1,1],1,1)) # 10
print(Solution().countSubarrays([1,3,5,2,7,1,2,5,7,7,7,1,2,3],1,5)) # 2

