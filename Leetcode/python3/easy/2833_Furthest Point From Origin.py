#
# @lc app=leetcode id=2833 lang=python3
#
# [2833] Furthest Point From Origin
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # return (lambda cnt: abs(cnt['R'] - cnt['L']) + cnt['_'])(Counter(moves))
        cnt = diff = 0
        for ch in moves:
            if ch =='L':
                diff -= 1
            elif ch == 'R':
                diff += 1
            else:
                cnt += 1
        return abs(diff) + cnt
# @lc code=end

