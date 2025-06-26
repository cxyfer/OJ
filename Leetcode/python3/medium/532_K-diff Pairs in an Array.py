#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        return (lambda cnt: sum(1 for x in cnt if (k > 0 and x + k in cnt) or (k == 0 and cnt[x] > 1)))(Counter(nums))
# @lc code=end

