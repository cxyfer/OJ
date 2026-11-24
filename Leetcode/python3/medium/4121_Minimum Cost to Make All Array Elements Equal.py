#
# @lc app=leetcode id=4121 lang=python3
#
# [4121] Minimum Cost to Make All Array Elements Equal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Weekly Contest 529 - Q2
1. 前後綴分解 + 分組循環預處理 prev 和 next (賽時寫法)
2. 分組循環
"""
# @lc code=start
class Solution1:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)

        prev = [0] * n
        i = n - 1
        while i >= 0:
            st = i
            while i >= 0 and nums[st] == nums[i]:
                i -= 1
            for j in range(i + 1, st + 1):
                prev[j] = i

        next = [n] * n
        i = 0
        while i < n:
            st = i
            while i < n and nums[st] == nums[i]:
                i += 1
            for j in range(st, i):
                next[j] = i

        ans = inf
        for i in range(1, n - 1):
            x = nums[i]
            pre = (prev[i] + 1) * x
            suf = (n - next[i]) * x
            ans = min(ans, pre + suf)
        return ans


class Solution2:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)

        ans = inf
        i = 0
        while i < n:
            st = i
            while i < n and nums[st] == nums[i]:
                i += 1
            if i - 1 > 0 and st < n - 1:
                ans = min(ans, (st) * nums[st] + (n - i) * nums[st])
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()
print(sol.minCost([1,2,3]))  # 4
print(sol.minCost([3,3,3,6,3,3]))  # 9