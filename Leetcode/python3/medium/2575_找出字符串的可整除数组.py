#
# @lc app=leetcode.cn id=2575 lang=python3
#
# [2575] 找出字符串的可整除数组
#
from preImport import *
# @lc code=start
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0] * n
        cur = 0
        for i, ch in enumerate(word):
            cur = (cur * 10 + int(ch)) % m
            ans[i] = 1 if cur == 0 else 0
        return ans
# @lc code=end

