#
# @lc app=leetcode id=910 lang=python3
# @lcpr version=30204
#
# [910] Smallest Range II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mn, mx = nums[0], nums[n - 1]
        ans = mx - mn
        for i in range(n - 1):
            ans = min(ans, max(nums[i] + k, mx - k) - min(nums[0] + k, nums[i + 1] - k))
        return ans
# @lc code=end



#
# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0,10]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,6]\n3\n
# @lcpr case=end

#

