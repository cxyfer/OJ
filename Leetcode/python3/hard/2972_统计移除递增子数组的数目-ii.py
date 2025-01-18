#
# @lc app=leetcode.cn id=2972 lang=python3
#
# [2972] 统计移除递增子数组的数目 II
#
from preImport import *
# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        # return self.solve1(nums)
        return self.solve2(nums)
    """
        1. 雙指標 (簡潔版)
        枚舉右端點，移動左端點
    """
    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]: # 先確定前綴的最長遞增陣列的最後一個元素的下標
            i += 1
        if i == n - 1: # 特判，整個陣列都是遞增的，代表每個子陣列都是可以被移除的
            return n * (n + 1) // 2

        ans = i + 2 # 可以移除 [0,n-1], [1,n-1], ..., [i+1, n-1] 的子陣列
        j = n - 1
        while j == n - 1 or nums[j] < nums[j + 1]: # 枚舉右端點
            while i >= 0 and nums[i] >= nums[j]: # 左端點太大了，移動左端點
                i -= 1
            ans += i + 2 # 可以移除 [0,j-1], [1,j-1], ..., [i+1, j-1] 的子陣列
            j -= 1
        return ans
    """
        2. 雙指標 + 賽時寫的
    """
    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [1]
        for i in range(1, n):
            x = 1 if nums[i] > nums[i - 1] and pre[-1] else 0
            pre.append(x)
        suf = [1]
        for i in range(n - 2, -1, -1):
            x = 1 if nums[i] < nums[i + 1] and suf[-1] else 0
            suf.append(x)
        suf = suf[::-1]

        i = pre.count(1) - 1 # 前綴最長遞增陣列的最後一個元素的下標
        if i == n - 1:
            return n * (n + 1) // 2
        ans = i + 2 # 可以移除 [0,n-1], [1,n-1], ..., [i+1, n-1] 的子陣列
        j = n - 1
        while j > 0 and suf[j] == 1: # 枚舉右端點
            while i >= 0 and nums[i] >= nums[j]: # 左端點太大了，移動左端點
                i -= 1
            ans += i + 2 # 可以移除 [0,j-1], [1,j-1], ..., [i+1, j-1] 的子陣列
            j -= 1
        return ans
# @lc code=end

