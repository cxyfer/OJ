#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

from preImport import *
# @lc code=start
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        return len(s) == len(t) and Counter(s) == Counter(t)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
        return all(v == 0 for v in cnt.values())

# Solution = Solution1
Solution = Solution2
# @lc code=end

