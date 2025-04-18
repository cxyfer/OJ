#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
式子變換 + 正難則反
j - i != nums[j] - nums[i]
j - nums[j] != i - nums[i]
"""
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        ans = n * (n - 1) // 2
        for j, y in enumerate(nums):
            ans -= cnt[j - y]
            cnt[j - y] += 1
        return ans
# @lc code=end

