#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#


# @lcpr-template-start
from preImport import *


# @lcpr-template-end
# @lc code=start
class Solution1a:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # f[i][j] 表示從 (i, j) 到最底層的最小路徑和
        @cache
        def f(i: int, j: int) -> int:
            if i == n:
                return 0
            return triangle[i][j] + min(f(i + 1, j), f(i + 1, j + 1))
        return f(0, 0)

class Solution1b:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * (i + 1) for i in range(n)]
        f[n - 1] = triangle[-1][::]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[i][j] = triangle[i][j] + min(f[i + 1][j], f[i + 1][j + 1])
        return f[0][0]

class Solution1c:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = triangle[-1][::]
        for i in range(n - 2, -1, -1):
            nf = [-1] * (i + 1)
            for j in range(i + 1):
                nf[j] = triangle[i][j] + min(f[j], f[j + 1])
            f = nf
        return f[0]

class Solution1d:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = triangle[-1][::]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                f[j] = triangle[i][j] + min(f[j], f[j + 1])
        return f[0]

class Solution2a:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        # f[i][j] 表示從 (i, j) 到最頂層的最小路徑和
        def f(i: int, j: int) -> int:
            if i < 0:
                return 0 if j == 0 else float("inf")
            if j < 0 or j >= i + 1:
                return float("inf")
            return triangle[i][j] + min(f(i - 1, j), f(i - 1, j - 1))
        return min(f(n - 1, j) for j in range(n))

class Solution2b:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * (i + 1) for i in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                f[i][j] = triangle[i][j] + min(
                    f[i - 1][j] if j < i else float("inf"),
                    f[i - 1][j - 1] if j > 0 else float("inf"),
                )
        return min(f[n - 1])

class Solution2d:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i, -1, -1):
                f[j] = triangle[i][j] + min(
                    f[j] if j < i else float("inf"),
                    f[j - 1] if j > 0 else float("inf"),
                )
        return min(f)

# Solution = Solution1a
# Solution = Solution1b
# Solution = Solution1c
# Solution = Solution1d
# Solution = Solution2a
# Solution = Solution2b
Solution = Solution2d
# @lc code=end

sol = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
# print(sol.minimumTotal([[-10]]))  # -10
