#
# @lc app=leetcode id=3392 lang=python3
# @lcpr version=30204
#
# [3392] Count Subarrays of Length Three With a Condition
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            if 2 * (nums[i] + nums[i+2]) == nums[i+1]:
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,1,4,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

#

