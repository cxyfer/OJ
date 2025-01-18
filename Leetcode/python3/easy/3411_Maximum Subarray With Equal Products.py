#
# @lc app=leetcode id=3411 lang=python3
# @lcpr version=30204
#
# [3411] Maximum Subarray With Equal Products
#


# @lcpr-template-start
from preImport import *
from operator import mul
from functools import reduce
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for ln in range(1, n + 1):
            for i in range(n - ln + 1):
                subarray = nums[i:i + ln]
                if reduce(mul, subarray) == gcd(*subarray) * lcm(*subarray):
                    ans = max(ans, ln)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,1,2,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,4,5,1]\n
# @lcpr case=end

#

