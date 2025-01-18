#
# @lc app=leetcode id=859 lang=python3
# @lcpr version=30204
#
# [859] Buddy Strings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def buddyStrings(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        cnt1, cnt2 = [0] * 26, [0] * 26
        diff = 0
        for ch1, ch2 in zip(s, t):
            cnt1[ord(ch1) - ord('a')] += 1
            cnt2[ord(ch2) - ord('a')] += 1
            if ch1 != ch2:
                diff += 1
        if diff == 2:
            return cnt1 == cnt2
        return diff == 0 and any(ch > 1 for ch in cnt1)
# @lc code=end

#
# @lcpr case=start
# "ab"\n"ba"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aa"\n
# @lcpr case=end

#

