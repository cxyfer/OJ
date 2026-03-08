#
# @lc app=leetcode id=3863 lang=python3
#
# [3863] Minimum Operations to Sort a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(x <= y for x, y in pairwise(s)):
            return 0
        if n == 2:
            return -1

        cnt = Counter(s)
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if s[0] == mx and s[-1] == mn and cnt[mx] == 1 and cnt[mn] == 1:
            return 3
        return 2
# @lc code=end

