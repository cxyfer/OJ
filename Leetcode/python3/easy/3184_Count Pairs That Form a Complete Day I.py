#
# @lc app=leetcode id=3184 lang=python3
# @lcpr version=30203
#
# [3184] Count Pairs That Form a Complete Day I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [12,12,30,24,24]\n
# @lcpr case=end

# @lcpr case=start
# [72,48,24,3]\n
# @lcpr case=end

#

