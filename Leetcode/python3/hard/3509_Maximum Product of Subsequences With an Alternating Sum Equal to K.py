#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        suf0 = [0] * n
        suf0[n - 1] = int(nums[n - 1] == 0)
        for i in range(n - 2, -1, -1):
            suf0[i] = suf0[i + 1] + int(nums[i] == 0)
        
        @cache
        def f(i: int, s: int, p: int, pos: int, taken: bool, has0: bool) -> int:
            if i == n:
                return p if s == k and taken else -1
            if p == 0 and suf0[i] == 0 and not has0:
                return -1
            if p == 0 and suf0[i] == 1 and nums[i] == 0 and not has0:
                return f(i + 1, s, 0, pos ^ 1, True, True)
            res = f(i + 1, s, p, pos, taken, has0)
            if p * nums[i] <= limit:
                res = max(res, f(i + 1, s + (nums[i] if pos & 1 else -nums[i]), p * nums[i], pos ^ 1, True, has0 or nums[i] == 0))
            if p * nums[i] > limit and suf0[i] > 0:
                res = max(res, f(i + 1, s + (nums[i] if pos & 1 else -nums[i]), 0, pos ^ 1, True, has0 or nums[i] == 0))
            return res

        ans = f(0, 0, 1, 1, False, False)
        f.cache_clear()
        return ans
# @lc code=end

sol = Solution()
print(sol.maxProduct([1,2,3], 2, 10))  # 6
print(sol.maxProduct([0,2,3], -5, 12))  # -1
print(sol.maxProduct([2,2,3,3], 0, 9))  # 9
print(sol.maxProduct([0], 0, 10))  # 0
print(sol.maxProduct([1,0], 0, 30))  # 0
print(sol.maxProduct([10,10,9,0], 1, 20))  # 0
print(sol.maxProduct([12,3,3,0,2], 11, 20))  # -1
print(sol.maxProduct([0,5], 0, 10))  # 0
