#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q1, q2 = deque(), deque()
        n = len(senate)
        for i, ch in enumerate(senate):
            if ch == 'R':
                q1.append(i)
            else:
                q2.append(i)
        while q1 and q2:
            if q1[0] < q2[0]: # 一名Radiant 禁用了 一名Dire 
                q1.append(q1.popleft() + n) # 該Radiant可以進入下一輪
                q2.popleft()
            else:
                q2.append(q2.popleft() + n)
                q1.popleft()
        return "Radiant" if q1 else "Dire"
# @lc code=end

