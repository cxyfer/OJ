#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    """
        Two pointers
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        slow, fast = 0, 0
        while slow < m and fast < n:
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        return slow == m
# @lc code=end

