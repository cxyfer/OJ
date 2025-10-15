#
# @lc app=leetcode id=3712 lang=python3
#
# [3712] Sum of Elements With Frequency Divisible by K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        ans = 0
        for x, v in cnt.items():
            if v % k == 0:
                ans += x * v
        return ans
# @lc code=end

