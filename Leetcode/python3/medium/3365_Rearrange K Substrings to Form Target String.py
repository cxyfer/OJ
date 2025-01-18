#
# @lc app=leetcode id=3365 lang=python3
# @lcpr version=30204
#
# [3365] Rearrange K Substrings to Form Target String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        ln1, ln2 = len(s) // k, len(t) // k
        cnt1 = Counter([s[i:i+ln1] for i in range(0, len(s), ln1)])
        cnt2 = Counter([t[i:i+ln2] for i in range(0, len(t), ln2)])
        return cnt1 == cnt2
# @lc code=end



#
# @lcpr case=start
# "abcd"\n"cdab"\n2\n
# @lcpr case=end

# @lcpr case=start
# "aabbcc"\n"bbaacc"\n3\n
# @lcpr case=end

# @lcpr case=start
# "aabbcc"\n"bbaacc"\n2\n
# @lcpr case=end

#

