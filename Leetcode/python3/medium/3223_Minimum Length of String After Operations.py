#
# @lc app=leetcode id=3223 lang=python3
# @lcpr version=30204
#
# [3223] Minimum Length of String After Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        ans = 0
        for i in range(26):
            if cnt[i] >= 3:
                ans += 1 if cnt[i] & 1 else 2
            else:
                ans += cnt[i]
        return ans
# @lc code=end



#
# @lcpr case=start
# "abaacbcbb"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

#

