#
# @lc app=leetcode id=3380 lang=python3
# @lcpr version=30204
#
# [3380] Maximum Area Rectangle With Point Constraints I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        s = set(tuple(point) for point in points)
        ans = -1
        for comb in combinations(points, 4):
            X = sorted(set(point[0] for point in comb))
            Y = sorted(set(point[1] for point in comb))
            if len(X) != 2 or len(Y) != 2:
                continue
            corners = {(X[0], Y[0]), (X[0], Y[1]), (X[1], Y[0]), (X[1], Y[1])}
            if set(tuple(point) for point in comb) != corners:
                continue
            others = s - corners
            for px, py in others:
                if X[0] <= px <= X[1] and Y[0] <= py <= Y[1]:
                    break
            else:
                ans = max(ans, (X[1] - X[0]) * (Y[1] - Y[0]))
        return ans
# @lc code=end

sol = Solution()
print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3]])) # 4
print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3],[2,2]])) # -1
print(sol.maxRectangleArea([[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]])) # 2
#
# @lcpr case=start
# [[1,1],[1,3],[3,1],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,3],[3,1],[3,3],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]\n
# @lcpr case=end

#

