#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        Sliding window
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur = sum(nums[:k])
        ans = cur
        for idx in range(k, n):
            cur += nums[idx] - nums[idx-k] # sliding window
            ans = max(ans, cur)
        return ans / k
# @lc code=end

