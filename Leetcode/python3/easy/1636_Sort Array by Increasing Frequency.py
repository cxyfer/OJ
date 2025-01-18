#
# @lc app=leetcode id=1636 lang=python3
# @lcpr version=30204
#
# [1636] Sort Array by Increasing Frequency
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return sorted(nums, key = lambda x : (cnt[x], -x))
# @lc code=end



#
# @lcpr case=start
# [1,1,2,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,-6,4,5,-6,1,4,1]\n
# @lcpr case=end

#

