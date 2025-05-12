#
# @lc app=leetcode id=3545 lang=python3
#
# [3545] Minimum Deletions for At Most K Distinct Characters
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        ans = 0
        cnt = Counter(s)
        for _, v in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
            if k > 0:
                k -= 1
            else:
                ans += v
        return ans
# @lc code=end

