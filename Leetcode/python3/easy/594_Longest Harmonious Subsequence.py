#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for k, v in cnt.items():
            if k + 1 in cnt:
                ans = max(ans, v + cnt[k + 1])
        return ans
# @lc code=end

