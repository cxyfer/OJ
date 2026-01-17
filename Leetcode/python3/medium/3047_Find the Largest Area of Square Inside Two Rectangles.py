#
# @lc app=leetcode id=3047 lang=python3
#
# [3047] Find the Largest Area of Square Inside Two Rectangles
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
max = lambda x, y: x if x > y else y
min = lambda x, y: x if x < y else y
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_w = 0
        for i, ((bx1, by1), (tx1, ty1)) in enumerate(zip(bottomLeft, topRight)):
            for j in range(i):
                ((bx2, by2), (tx2, ty2)) = bottomLeft[j], topRight[j]
                bx = max(bx1, bx2)
                by = max(by1, by2)
                tx = min(tx1, tx2)
                ty = min(ty1, ty2)
                max_w = max(max_w, min(tx - bx, ty - by))
        return max_w * max_w
# @lc code=end

sol = Solution()
print(sol.largestSquareArea([[1,1],[2,2],[3,1]], [[3,3],[4,4],[6,6]]))  # 1