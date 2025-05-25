#
# @lc app=leetcode id=3557 lang=python3
#
# [3557] Find Maximum Number of Non Intersecting Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        pos = defaultdict(list)
        for i, c in enumerate(word):
            pos[c].append(i)

        @cache
        def f(i):
            if i == n:
                return 0
            c = word[i]
            res = f(i + 1)
            j = bisect_left(pos[c], i + 3)
            if j < len(pos[c]):
                res = max(res, f(pos[c][j] + 1) + 1)
            return res
        return f(0)
# @lc code=end

sol = Solution()
print(sol.maxSubstrings("abcdeafdef"))  # 2
print(sol.maxSubstrings("bcdaaaab"))  # 1