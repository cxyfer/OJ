#
# @lc app=leetcode id=3340 lang=python3
# @lcpr version=30204
#
# [3340] Check Balanced String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isBalanced(self, num: str) -> bool:
        # return sum((ord(d) - ord('0')) * (-1 if i & 1 else 1) for i, d in enumerate(num)) == 0
        cnt = [0, 0]
        for i, ch in enumerate(num):
            cnt[i & 1] += ord(ch) - ord('0')
        return cnt[0] == cnt[1]
# @lc code=end



#
# @lcpr case=start
# "1234"\n
# @lcpr case=end

# @lcpr case=start
# "24123"\n
# @lcpr case=end

#

