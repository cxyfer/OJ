#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
# 基础算法精讲 01 - Two pointers

Extend from 167. Sum of Two Numbers II - Input Ordered Array
i < left < right < n

一些優化：
1. 如果 nums[i] > 0，後面的數字都會大於 0，不可能有三個數字相加等於 0，可以終止迴圈
2. 如果 nums[i] + nums[i+1] + nums[i+2] > 0，則後面任三個數字相加都會大於 0，不可能有三個數字相加等於 0，可以終止迴圈
3. 如果 nums[i] + nums[n-2] + nums[n-1] < 0，則可以跳過 nums[i] ，因為 nums[i] + nums[left] + nums[right] 只會更小
    - 注意這種情況下，枚舉 i 後面的數字仍然有可能有答案，故只需要跳過 i 即可

TS: O(n log n + n^2) = O(n^2)
SC: O(1), ignore the space of sorting
"""
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        ans = []
        nums.sort()
        # i < left < right < n
        for i in range(n - 2):  # 枚舉第一個數字 nums[i]
            if i > 0 and nums[i] == nums[i-1]:  # 和前一個數字相同，由於題目要求不能有重複數字，跳過
                continue
            if nums[i] > 0:  # 優化 1
                break
            if nums[i] + nums[i+1] + nums[i+2] > 0:  # 優化 2
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:  # 優化 3
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:  # 太小了，左邊的數字太小，往右移
                    left += 1
                elif s > 0:  # 太大了，右邊的數字太大，往左移
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # 跳過重複答案
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 找下一個答案
                    left += 1
                    right -= 1
        return ans
# @lc code=end

