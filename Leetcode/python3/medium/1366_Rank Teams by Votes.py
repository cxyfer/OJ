#
# @lc app=leetcode id=1366 lang=python3
#
# [1366] Rank Teams by Votes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m = len(votes[0])
        cnts = defaultdict(lambda: [0] * m)
        for vote in votes:
            for i, ch in enumerate(vote):
                cnts[ch][i] += 1
        return ''.join(sorted(cnts, key=lambda ch: (cnts[ch], -ord(ch)), reverse=True))
# @lc code=end

sol = Solution()
print(sol.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
print(sol.rankTeams(["WXYZ","XYZW"]))
print(sol.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))