#
# @lc app=leetcode id=3185 lang=python3
# @lcpr version=30203
#
# [3185] Count Pairs That Form a Complete Day II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        cnt = [0] * 24
        for x in hours:
            x %= 24
            ans += cnt[24 - x] if x != 0 else cnt[0]
            # ans += cnt[(24 - x) % 24]
            cnt[x] += 1
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

