#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            cnt1 = cnt2 = 0  # 將 top/bottom 變成 x 的次數
            for t, b in zip(tops, bottoms):
                if t == x and b == x:
                    continue
                elif t == x:
                    cnt1 += 1
                elif b == x:
                    cnt2 += 1
                else:
                    return float('inf')
            return min(cnt1, cnt2)

        ans = min(check(tops[0]), check(bottoms[0]))
        return ans if ans != float('inf') else -1
# @lc code=end

