#
# @lc app=leetcode id=2717 lang=python3
# @lcpr version=30204
#
# [2717] Semi-Ordered Permutation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(1)
        j = nums.index(n)
        return i + (n - j - 1) - (i > j)
# @lc code=end



#
# @lcpr case=start
# [2,1,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,4,2,5]\n
# @lcpr case=end

#

