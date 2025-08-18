#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        q = [deque(), deque()]
        for i, c in enumerate(senate):
            q[c == 'D'].append(i)
        while all(q):
            r, d = q
            if r[0] < d[0]:
                r.append(r.popleft() + n)
                d.popleft()
            else:
                d.append(d.popleft() + n)
                r.popleft()
        return 'Radiant' if q[0] else 'Dire'
# @lc code=end

