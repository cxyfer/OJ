#
# @lc app=leetcode id=2255 lang=python3
#
# [2255] Count Prefixes of a Given String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # return sum(s.startswith(w) for w in words)
        ans = 0
        for w in words:
            if len(w) > len(s):
                continue
            for i, ch in enumerate(w):
                if ch != s[i]:
                    break
            else:
                ans += 1
        return ans
# @lc code=end

