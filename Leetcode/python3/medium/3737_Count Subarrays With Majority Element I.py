#
# @lc app=leetcode id=3737 lang=python3
#
# [3737] Count Subarrays With Majority Element I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = list(accumulate((1 if (x == target) else -1 for x in nums), initial=0))
        return sum(s[j] - s[i] > 0 for i in range(n) for j in range(i + 1, n + 1))
# @lc code=end

