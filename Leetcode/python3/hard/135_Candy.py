#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        suf = [1] * n 
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                suf[i] = suf[i + 1] + 1
        ans = pre = 0
        for i, x in enumerate(ratings):
            if i > 0 and x > ratings[i - 1]:
                pre += 1
            else:
                pre = 1
            ans += max(pre, suf[i])
        return ans
# @lc code=end

