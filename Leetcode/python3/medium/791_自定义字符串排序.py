#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#
from preImport import *
# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        ans = ''
        for ch in order:
            ans += ch * cnt[ord(ch) - ord('a')]
            cnt[ord(ch) - ord('a')] = 0
        for i in range(26):
            ans += chr(i + ord('a')) * cnt[i]
        return ans
# @lc code=end

