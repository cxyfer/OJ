#
# @lc app=leetcode id=541 lang=python3
# @lcpr version=30204
#
# [541] Reverse String II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        for i in range(0, n, 2 * k):
            s[i:i+k] = s[i:i+k][::-1]
        return "".join(s)
# @lc code=end



#
# @lcpr case=start
# "abcdefg"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

#

