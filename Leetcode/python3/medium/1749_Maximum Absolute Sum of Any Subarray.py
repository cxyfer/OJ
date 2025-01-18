#
# @lc app=leetcode id=1749 lang=python3
# @lcpr version=30203
#
# [1749] Maximum Absolute Sum of Any Subarray
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return self.solve1(nums)
        # return self.solve2(nums)

    def solve1(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * (n + 1)  # 正數
        dp2 = [0] * (n + 1)  # 負數
        for i, x in enumerate(nums, start=1):
            dp1[i] = max(dp1[i - 1] + x, x)
            dp2[i] = min(dp2[i - 1] + x, x)
        return max(max(dp1), abs(min(dp2)))

    def solve2(self, nums: List[int]) -> int:
        n = len(nums)
        res1, res2 = 0, 0
        f1, f2 = 0, 0
        for x in nums:
            f1, f2 = max(f1 + x, x), min(f2 + x, x)
            res1, res2 = max(res1, f1), min(res2, f2)
        return max(res1, abs(res2))
# @lc code=end

sol = Solution()
print(sol.maxAbsoluteSum([1,-3,2,3,-4])) # 5
print(sol.maxAbsoluteSum([2,-5,1,-4,3,-2])) # 8

#
# @lcpr case=start
# [1,-3,2,3,-4]\n
# @lcpr case=end

# @lcpr case=start
# [2,-5,1,-4,3,-2]\n
# @lcpr case=end

#
