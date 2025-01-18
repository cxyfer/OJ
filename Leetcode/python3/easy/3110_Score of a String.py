#
# @lc app=leetcode id=3110 lang=python3
# @lcpr version=30203
#
# [3110] Score of a String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        # return sum(abs(x - y) for x, y in pairwise(map(ord, s)))
        n = len(s)
        ans = 0
        for i in range(1, n):
            ans += abs(ord(s[i]) - ord(s[i - 1]))
        return ans
# @lc code=end



#
# @lcpr case=start
# "hello"\n
# @lcpr case=end

# @lcpr case=start
# "zaz"\n
# @lcpr case=end

#

