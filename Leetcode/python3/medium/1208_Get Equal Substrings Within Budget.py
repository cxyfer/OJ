#
# @lc app=leetcode id=1208 lang=python3
# @lcpr version=30202
#
# [1208] Get Equal Substrings Within Budget
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        典型的滑動窗口問題
    """
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        ans = 0
        cost = 0
        left = 0
        for right in range(n):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end



#
# @lcpr case=start
# "abcd"\n"bcdf"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"cdef"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"acde"\n0\n
# @lcpr case=end

#

