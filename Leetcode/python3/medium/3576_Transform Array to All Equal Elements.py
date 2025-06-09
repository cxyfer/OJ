#
# @lc app=leetcode id=3576 lang=python3
#
# [3576] Transform Array to All Equal Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def check(x):
            tmp = nums.copy()
            cnt = 0
            for i in range(n - 1):
                if tmp[i] != x:
                    tmp[i] *= -1
                    tmp[i + 1] *= -1
                    cnt += 1
            if tmp[n - 1] != x:
                return float("inf")
            return cnt
        return min(check(-1), check(1)) <= k
# @lc code=end

