#
# @lc app=leetcode id=908 lang=python3
# @lcpr version=30204
#
# [908] Smallest Range I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mx, mn = max(nums), min(nums)
        return max(0, mx - mn - 2 * k)
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

