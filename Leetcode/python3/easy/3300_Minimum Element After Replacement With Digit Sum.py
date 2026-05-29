#
# @lc app=leetcode id=3300 lang=python3
#
# [3300] Minimum Element After Replacement With Digit Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minElement(self, nums: List[int]) -> int:
        # return min(sum(map(int, str(x))) for x in nums)
        ans = float('inf')
        for x in nums:
            y = 0
            while x:
                x, r = divmod(x, 10)
                y += r
            ans = min(ans, y)
        return ans
# @lc code=end

