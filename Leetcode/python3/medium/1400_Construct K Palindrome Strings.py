#
# @lc app=leetcode id=1400 lang=python3
# @lcpr version=30204
#
# [1400] Construct K Palindrome Strings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)
        odd = sum(1 for v in cnt.values() if v & 1)
        return odd <= k <= len(s)
# @lc code=end



#
# @lcpr case=start
# "annabelle"\n2\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n3\n
# @lcpr case=end

# @lcpr case=start
# "true"\n4\n
# @lcpr case=end

#

