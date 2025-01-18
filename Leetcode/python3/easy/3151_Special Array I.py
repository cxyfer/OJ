#
# @lc app=leetcode id=3151 lang=python3
# @lcpr version=30202
#
# [3151] Special Array I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # return all(x & 1 != y & 1 for x, y in pairwise(nums))
        n = len(nums)
        for i in range(1, n):
            if nums[i] & 1 == nums[i - 1] & 1:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,6]\n
# @lcpr case=end

#

