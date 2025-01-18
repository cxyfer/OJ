#
# @lc app=leetcode id=643 lang=python3
# @lcpr version=30204
#
# [643] Maximum Average Subarray I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -float('inf')
        cur = 0
        for idx, x in enumerate(nums):
            cur += x
            if idx < k - 1:
                continue
            ans = max(ans, cur)
            cur -= nums[idx - k + 1]
        return ans / k
# @lc code=end

sol = Solution()
print(sol.findMaxAverage([-1], 1)) # -1

#
# @lcpr case=start
# [1,12,-5,-6,50,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n
# @lcpr case=end

#

