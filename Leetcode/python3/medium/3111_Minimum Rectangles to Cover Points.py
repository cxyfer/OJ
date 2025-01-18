#
# @lc app=leetcode id=3111 lang=python3
# @lcpr version=30204
#
# [3111] Minimum Rectangles to Cover Points
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Greedy
        由於矩形的高度沒有限制，所以只要考慮橫座標即可。
        為使矩形數量最少，我們應該讓每個矩形的橫座標範圍盡可能大，
        因此對於最左邊的的點 (st, y) ，應該建立一個從 x = st 到 x = st + w 的矩形。
    """
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort(key=lambda x: x[0])
        ans = 0
        last = -float('inf') # 上一個矩形的右邊界
        for x, y in points:
            if x > last:
                ans += 1
                last = x + w
        return ans
# @lc code=end



#
# @lcpr case=start
# [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[2,3],[1,2]]\n0\n
# @lcpr case=end

#

