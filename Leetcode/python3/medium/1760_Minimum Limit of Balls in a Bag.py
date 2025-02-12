#
# @lc app=leetcode id=1760 lang=python3
# @lcpr version=30204
#
# [1760] Minimum Limit of Balls in a Bag
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(k):
            # return sum(math.ceil(x / k) - 1 for x in nums) <= maxOperations
            return sum((x - 1) // k for x in nums) <= maxOperations
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end

#
# @lcpr case=start
# [9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,4,8,2]\n4\n
# @lcpr case=end

#

