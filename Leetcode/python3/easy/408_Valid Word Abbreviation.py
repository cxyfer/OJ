#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = 0
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                x = ord(abbr[j]) - ord('0')
                if x == 0: return False
                j += 1
                while j < n and abbr[j].isdigit():
                    x = x * 10 + ord(abbr[j]) - ord('0')
                    j += 1
                i += x
            else:
                return False
        return i == m and j == n
# @lc code=end

sol = Solution()
print(sol.validWordAbbreviation("internationalization", "i12iz4n"))  # True
print(sol.validWordAbbreviation("abbde", "a1b01e"))  # False