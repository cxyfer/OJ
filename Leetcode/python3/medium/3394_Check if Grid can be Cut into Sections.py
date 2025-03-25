#
# @lc app=leetcode id=3394 lang=python3
# @lcpr version=30204
#
# [3394] Check if Grid can be Cut into Sections
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    1. Line Sweep
    2. Merge Intervals
"""
# @lc code=start
class Solution1:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        X, Y = defaultdict(int), defaultdict(int)
        for x1, y1, x2, y2 in rectangles:
            X[x1 + 0.1] += 1
            X[x2 - 0.1] -= 1
            Y[y1 + 0.1] += 1
            Y[y2 - 0.1] -= 1
        
        def check(mp):
            res = cur = 0
            for k, v in sorted(mp.items()):
                cur += v
                if cur == 0:
                    res += 1
            return res >= 3

        return check(X) or check(Y)
    
class Solution2:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        X, Y = [], []
        for x1, y1, x2, y2 in rectangles:
            X.append((x1, x2))
            Y.append((y1, y2))
        
        def check(intervals):
            intervals.sort(key=lambda x: x[0])
            res = []
            for x, y in intervals:
                if not res or res[-1][1] <= x:
                    res.append([x, y])
                else:
                    res[-1][1] = max(res[-1][1], y)
            return len(res)

        return check(X) >= 3 or check(Y) >= 3

Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))  # True
print(sol.checkValidCuts(4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))  # True
print(sol.checkValidCuts(4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))  # False
# Add missing test case
print(sol.checkValidCuts(6, [[4,0,5,2],[0,5,4,6],[4,5,6,6]]))  # False

#
# @lcpr case=start
# 5\n[[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]\n
# @lcpr case=end

#

