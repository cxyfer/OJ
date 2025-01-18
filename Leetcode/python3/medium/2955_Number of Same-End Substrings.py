#
# @lc app=leetcode id=2955 lang=python3
# @lcpr version=30204
#
# [2955] Number of Same-End Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        cnt = [[0] * (n + 1) for _ in range(26)]
        for i, ch in enumerate(s):
            for j in range(26):
                cnt[j][i + 1] = cnt[j][i] + (1 if ord(ch) - ord("a") == j else 0)

        ans = []
        for l, r in queries:
            cur = 0
            for row in cnt:
                have = row[r + 1] - row[l]
                cur += have * (have + 1) // 2
            ans.append(cur)

        return ans
# @lc code=end

sol = Solution()
print(sol.sameEndSubstringCount("abcaab", [[0, 0], [1, 4], [2, 5], [0, 5]]))
print(sol.sameEndSubstringCount("abcd", [[0, 3]]))

#
# @lcpr case=start
# "abcaab"\n[[0,0],[1,4],[2,5],[0,5]]\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n[[0,3]]\n
# @lcpr case=end

#

