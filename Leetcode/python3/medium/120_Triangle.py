#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def f(i: int, j: int) -> int:
            if i == n:
                return 0
            return triangle[i][j] + min(f(i + 1, j), f(i + 1, j + 1))
        return f(0, 0)

class Solution2a:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[n - 1] = triangle[-1][::]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[i][j] = triangle[i][j] + min(f[i + 1][j], f[i + 1][j + 1])
        return f[0][0]

class Solution2b:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = triangle[-1][::]
        for i in range(n - 2, -1, -1):
            nf = [-1] * (i + 1)
            for j in range(i + 1):
                nf[j] = triangle[i][j] + min(f[j], f[j + 1])
            f = nf
        return f[0]

class Solution2c:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = triangle[-1][::]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[j] = triangle[i][j] + min(f[j], f[j + 1])
        return f[0]

# Solution = Solution1
# Solution = Solution2a
# Solution = Solution2b
Solution = Solution2c
# @lc code=end

sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # 11
print(sol.minimumTotal([[-10]]))  # -10

