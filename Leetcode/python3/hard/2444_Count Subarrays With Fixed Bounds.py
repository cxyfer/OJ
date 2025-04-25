#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 分組循環 + Sliding Window 
2. 一次遍歷的簡潔寫法，在遍歷時維護每組的左界
修改自靈神的題解：
https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/solutions/1895713/jian-ji-xie-fa-pythonjavacgo-by-endlessc-gag2/
"""
# @lc code=start
class Solution1:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        # 分組循環，使每組的數字都滿足 minK <= nums[i] <= maxK
        i = 0
        groups = []
        while i < n:
            if nums[i] < minK or nums[i] > maxK:
                i += 1
                continue
            st = i
            while i + 1 < n and minK <= nums[i+1] <= maxK:
                i += 1
            groups.append((st, i))
            i += 1
        # 對每組進行 Sliding Window
        ans = 0
        for st, ed in groups:
            mx = mn = st - 1
            for right in range(st, ed + 1):
                if nums[right] == minK:
                    mn = right
                if nums[right] == maxK:
                    mx = right
                left = min(mn, mx)
                ans += left - st + 1
        return ans
    
class Solution2:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
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
    
Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
