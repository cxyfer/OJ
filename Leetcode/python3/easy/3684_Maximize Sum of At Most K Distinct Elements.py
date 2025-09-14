#
# @lc app=leetcode id=3684 lang=python3
#
# [3684] Maximize Sum of At Most K Distinct Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # return sorted(set(nums), reverse=True)[:k]
        return heapq.nlargest(k, set(nums))
# @lc code=end

