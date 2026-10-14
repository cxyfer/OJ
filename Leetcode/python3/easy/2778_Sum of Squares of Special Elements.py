#
# @lc app=leetcode id=2778 lang=python3
#
# [2778] Sum of Squares of Special Elements 
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(x * x for i, x in enumerate(nums, 1) if len(nums) % i == 0)


class Solution2:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                ans += nums[i - 1] ** 2
                if i != n // i:
                    ans += nums[n // i - 1] ** 2
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end

