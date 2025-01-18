#
# @lc app=leetcode.cn id=2970 lang=python3
#
# [2970] 统计移除递增子数组的数目 I
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. Brute force
        Time: O(n^3)
    """
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        # return self.solve1(nums) 
        return self.solve2(nums)
    def solve1(self, nums: List[int]) -> int:
        def check(i, j):
            cur = nums[:i] + nums[j + 1:]
            nn = len(cur)
            for k in range(nn - 1):
                if cur[k] >= cur[k + 1]:
                    return False
            return True
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    ans += 1
        return ans
    """
        2. 前後綴分解
        Time: O(n^2)
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
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if (i-1 < 0 or pre[i-1] == 1) and (j+1 >= n or suf[j+1] == 1) and (i-1 < 0 or j+1 >= n or nums[i-1] < nums[j+1]):
                    ans += 1
        return ans
# @lc code=end

