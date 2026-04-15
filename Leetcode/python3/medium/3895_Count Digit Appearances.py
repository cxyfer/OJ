#
# @lc app=leetcode id=3895 lang=python3
#
# [3895] Count Digit Appearances
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        # return sum(str(x).count(str(digit)) for x in nums)
        ans = 0
        for x in nums:
            while x >= 10:
                if x % 10 == digit:
                    ans += 1
                x //= 10
            if x == digit:
                ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.countDigitOccurrences([1023, 4506, 7890, 0], 0))
