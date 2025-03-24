#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def f(i: int, j: int) -> int:
            if i == n:
                return 0
            if j < 0 or j >= n:
                return float('inf')
            return matrix[i][j] + min(f(i + 1, j - 1), f(i + 1, j), f(i + 1, j + 1))
        return min(f(0, j) for j in range(n))
    
class Solution2a:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # f[i][j] 表示從 (i, j - 1) 開始的最小下降路徑和
        f = [[float('inf')] * (n + 2) for _ in range(n)]
        f[-1] = [float('inf')] + matrix[-1][::] + [float('inf')]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(matrix[i], 1):
                f[i][j] = x + min(f[i + 1][j - 1], f[i + 1][j], f[i + 1][j + 1])
        return min(f[0])

class Solution2b:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [float('inf')] + matrix[-1][::] + [float('inf')]
        for i in range(n - 2, -1, -1):
            nf = [float('inf')] * (n + 2)
            for j, x in enumerate(matrix[i], 1):
                nf[j] = x + min(f[j - 1], f[j], f[j + 1])
            f = nf
        return min(f)
    
class Solution2c:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [float('inf')] + matrix[-1][::] + [float('inf')]
        for i in range(n - 2, -1, -1):
            pre = f[0]  # 保存會被覆蓋掉的 f[j - 1]
            for j, x in enumerate(matrix[i], 1):
                pre, f[j] = f[j], x + min(pre, f[j], f[j + 1])
        return min(f)
    
# Solution = Solution1
# Solution = Solution2a
Solution = Solution2b
# Solution = Solution2c
# @lc code=end

sol = Solution()
print(sol.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))  # 13
print(sol.minFallingPathSum([[-19,57],[-40,-5]]))  # -59
