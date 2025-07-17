#
# @lc app=leetcode id=2915 lang=python3
#
# [2915] Length of the Longest Subsequence That Sums to Target
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
fmax = lambda x, y: x if x > y else y
class Solution1a:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # 目前會 TLE
        @cache
        def dfs(i, j):
            if j < 0:
                return float('-inf')
            if i < 0:
                return 0 if j == 0 else float('-inf')
            return fmax(dfs(i - 1, j), dfs(i - 1, j - nums[i]) + 1)
        ans = dfs(n - 1, target)
        dfs.cache_clear()
        return ans if ans > 0 else -1

class Solution1b:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [[float('-inf')] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(nums, start=1):
            for j in range(target + 1):
                if j >= x:
                    f[i][j] = fmax(f[i - 1][j], f[i - 1][j - x] + 1)
                else:
                    f[i][j] = f[i - 1][j]
        return f[n][target] if f[n][target] > 0 else -1
    
class Solution1c:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        f = [0] + [float('-inf')] * target
        for x in nums:
            for j in range(target, x - 1, -1):
                f[j] = fmax(f[j], f[j - x] + 1)
        return f[target] if f[target] > 0 else -1

# Solution = Solution1a
# Solution = Solution1b
Solution = Solution1c
# @lc code=end