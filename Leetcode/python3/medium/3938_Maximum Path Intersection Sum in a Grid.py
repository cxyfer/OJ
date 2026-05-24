#
# @lc app=leetcode id=3938 lang=python3
#
# [3938] Maximum Path Intersection Sum in a Grid
#

# @lcpr-template-start
from preImport import *
def debug(*args, **kwargs):
    print('\033[91m', end='')
    print(*args, **kwargs)
    print('\033[0m', end='')
# @lcpr-template-end

# @lc code=start
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = -inf
        for i, row in enumerate(grid):
            s = list(accumulate(row, initial=0))
            mn = inf
            for j, x in enumerate(s):
                ans = max(ans, x - mn)
                if j > 0:
                    mn = min(mn, s[j - 1])
            if 0 < i < m and n >= 3:
                ans = max(ans, max(row[1:-1]))
        for i, col in enumerate(zip(*grid)):
            s = list(accumulate(col, initial=0))
            mn = inf
            for j, x in enumerate(s):
                ans = max(ans, x - mn)
                if j > 0:
                    mn = min(mn, s[j - 1])
        return ans
# @lc code=end

sol = Solution()
print(sol.maxScore([[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]))  # 4
print(sol.maxScore([[4,-2,-3],[-1,-3,-1],[-4,2,-1]]))  # 3
print(sol.maxScore([[-13,2,-11,15],[-1,-14,3,-4],[6,-9,-12,-14],[1,20,-13,10],[-9,-6,-20,3],[20,-8,-17,-4],[7,12,12,-20],[13,-12,9,-11],[-18,1,5,4],[-6,16,1,11]]))  # 40
print(sol.maxScore([[-5,5,-5],[-5,-5,-5]]))  # 0
print(sol.maxScore([[-17,-3,-14,3,-10,-18,2,-5],[-19,8,4,-13,-1,13,-13,8],[5,4,-18,4,-13,-11,4,-15]]))  # 13
print(sol.maxScore([[-2,-3,2],[-2,5,-2],[-3,-4,-2]]))  # 5