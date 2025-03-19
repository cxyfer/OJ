#
# @lc app=leetcode id=3489 lang=python3
#
# [3489] Zero Array Transformation IV
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if all(x == 0 for x in nums):
            return 0
        f = [[True] + [False] * x for x in nums]
        for k, (l, r, v) in enumerate(queries):
            for i in range(l, r + 1):
                x = nums[i]
                if f[i][x]: continue
                for j in range(x, v - 1, -1):
                    f[i][j] |= f[i][j - v]
            if all(f[i][nums[i]] for i in range(n)):
                return k + 1
        return -1
    
class Solution2:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if all(x == 0 for x in nums):
            return 0
        f = [1] * n
        for k, (l, r, v) in enumerate(queries):
            for i in range(l, r + 1):
                if (f[i] >> nums[i]) & 1: continue
                f[i] |= f[i] << v
            if all((f[i] >> v) & 1 for i, v in enumerate(nums)):
                return k + 1
        return -1
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.minZeroArray([0], [[0,0,1]]))  # 0