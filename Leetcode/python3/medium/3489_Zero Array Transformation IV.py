#
# @lc app=leetcode id=3489 lang=python3
#
# [3489] Zero Array Transformation IV
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
背包 DP + 位運算優化
對於每個位置 i ，考慮是否能夠湊出 nums[i]
"""
# @lc code=start
class Solution1:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if all(x == 0 for x in nums):
            return 0
        # f[i][j] 表示第 i 個位置是否能夠湊出 j
        f = [[True] + [False] * x for x in nums]
        for k, (l, r, v) in enumerate(queries):
            # 更新 [l, r] 區間
            for i in range(l, r + 1):
                x = nums[i]
                if f[i][x]: continue  # 已經湊出 nums[i]
                for j in range(x, v - 1, -1):  # 從大到小更新 f[i][j]
                    f[i][j] |= f[i][j - v]
            # 檢查是否能夠湊出所有的 nums[i]
            if all(fi[v] for fi, v in zip(f, nums)):
                return k + 1
        return -1
    
class Solution2:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if all(x == 0 for x in nums):
            return 0
        # f[i] 表示第 i 個位置能夠湊出的所有可能值，用位運算表示
        f = [1] * n
        for k, (l, r, v) in enumerate(queries):
            # 更新 [l, r] 區間
            for i in range(l, r + 1):
                if (f[i] >> nums[i]) & 1: continue  # 已經湊出 nums[i]
                f[i] |= f[i] << v  # 更新 f[i]
            # 檢查是否能夠湊出所有的 nums[i]
            if all((fi >> v) & 1 for fi, v in zip(f, nums)):
                return k + 1
        return -1
    
# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.minZeroArray([0], [[0,0,1]]))  # 0