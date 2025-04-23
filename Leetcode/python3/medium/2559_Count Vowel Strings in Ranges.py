#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    Prefix Sum
"""
# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = set("aeiou")
        s = [0] * (n + 1)
        for i, w in enumerate(words):
            s[i + 1] = s[i] + (1 if w[0] in vowels and w[-1] in vowels else 0)
        return [s[r + 1] - s[l] for l, r in queries]
# @lc code=end

