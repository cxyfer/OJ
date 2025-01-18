#
# @lc app=leetcode id=3168 lang=python3
# @lcpr version=30203
#
# [3168] Minimum Number of Chairs in a Waiting Room
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = cur = 0
        for ch in s:
            if ch == 'E':
                cur += 1
                ans = max(ans, cur)
            else:
                cur -= 1
        return ans
# @lc code=end



#
# @lcpr case=start
# "EEEEEEE"\n
# @lcpr case=end

# @lcpr case=start
# "ELELEEL"\n
# @lcpr case=end

# @lcpr case=start
# "ELEELEELLL"\n
# @lcpr case=end

#

