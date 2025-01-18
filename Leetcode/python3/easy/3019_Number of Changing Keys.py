#
# @lc app=leetcode id=3019 lang=python3
# @lcpr version=30204
#
# [3019] Number of Changing Keys
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        ans = i = 0
        while i < n:
            st = i
            while i < n and s[i].lower() == s[st].lower():
                i += 1
            ans += 1
        return ans - 1
# @lc code=end



#
# @lcpr case=start
# "aAbBcC"\n
# @lcpr case=end

# @lcpr case=start
# "AaAaAaaA"\n
# @lcpr case=end

#

