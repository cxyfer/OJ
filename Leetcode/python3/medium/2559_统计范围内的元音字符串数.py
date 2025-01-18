#
# @lc app=leetcode.cn id=2559 lang=python3
#
# [2559] 统计范围内的元音字符串数
#
from preImport import *
# @lc code=start
class Solution:
    """
        Prefix Sum
    """
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = [0] * (len(words)+1)
        vowels = "aeiou"
        for i, w in enumerate(words):
            s[i+1] = s[i] + (1 if w[0] in vowels and w[-1] in vowels else 0)
        return [s[r+1] - s[l] for l, r in queries]
# @lc code=end

