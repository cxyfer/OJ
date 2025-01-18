#
# @lc app=leetcode id=521 lang=python3
# @lcpr version=30203
#
# [521] Longest Uncommon Subsequence I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1
# @lc code=end



#
# @lcpr case=start
# "aba"\n"cdc"\n
# @lcpr case=end

# @lcpr case=start
# "aaa"\n"bbb"\n
# @lcpr case=end

# @lcpr case=start
# "aaa"\n"aaa"\n
# @lcpr case=end

#

