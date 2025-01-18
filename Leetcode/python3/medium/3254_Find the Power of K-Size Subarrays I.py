#
# @lc app=leetcode id=3254 lang=python3
# @lcpr version=30204
#
# [3254] Find the Power of K-Size Subarrays I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * (n - k + 1)
        cnt = 0
        for i, x in enumerate(nums):
            if i == 0 or nums[i - 1] + 1 == nums[i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                ans[i - k + 1] = x
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,3,2,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,2,3,2]\n2\n
# @lcpr case=end

#

