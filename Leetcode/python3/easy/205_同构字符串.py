#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
from preImport import *
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mp = defaultdict(str)
        used = set()
        for i in range(n):
            if s[i] in mp:
                if mp[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                mp[s[i]] = t[i]
                used.add(t[i])
        return True
# @lc code=end

