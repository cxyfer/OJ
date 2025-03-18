#
# @lc app=leetcode id=2401 lang=python3
#
# [2401] Longest Nice Subarray
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    在子陣列中，每個位元只能出現一次
    1. 用 cnt 來記錄每個位元出現的次數、 over 來記錄有幾個位元出現超過一次
    2. 用 or_val 來記錄當前每個位元是否出現過
    3. LogTrick
"""
# @lc code=start
class Solution1:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = left = over = 0
        cnt = [0] * 32
        for right, x in enumerate(nums):
            # 1. 入窗口
            while x:
                lb = x & -x
                cnt[lb.bit_length() - 1] += 1
                if cnt[lb.bit_length() - 1] == 2:
                    over += 1
                x ^= lb
            # 2. 出窗口
            while over > 0:
                y = nums[left]
                while y:
                    lb = y & -y
                    cnt[lb.bit_length() - 1] -= 1
                    if cnt[lb.bit_length() - 1] == 1:
                        over -= 1
                    y ^= lb
                left += 1
            # 3. 更新答案
            ans = max(ans, right - left + 1)
        return ans
    
class Solution2:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # 用 or_val 來記錄當前每個位元是否出現過
        ans = left = or_val = 0
        for right, x in enumerate(nums):
            # 1. 要先出窗口才能入窗口
            while or_val & x:
                or_val ^= nums[left]
                left += 1
            # 2. 入窗口
            or_val |= x
            # 3. 更新答案
            ans = max(ans, right - left + 1)
        return ans

class Solution3:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        for right, or_val in enumerate(nums):
            left = right - 1
            while left >= 0 and (or_val & nums[left]) == 0:
                or_val |= nums[left]
                left -= 1
            ans = max(ans, right - left)
        return ans

class Solution(Solution1):
# class Solution(Solution2):
# class Solution(Solution3):
    pass
# @lc code=end

