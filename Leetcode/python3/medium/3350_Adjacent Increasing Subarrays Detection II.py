#
# @lc app=leetcode id=3350 lang=python3
#
# [3350] Adjacent Increasing Subarrays Detection II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 1
        pre, cur = 0, 1
        for x, y in pairwise(nums):
            if x < y:
                cur += 1
                ans = max(ans, min(pre, cur), cur // 2)
            else:
                pre, cur = cur, 1
            # ans = max(ans, min(pre, cur), cur // 2)
        return ans
# @lc code=end

sol = Solution()
print(sol.maxIncreasingSubarrays([5,8,-2,-1]))  # 2