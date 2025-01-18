#
# @lc app=leetcode id=1039 lang=python3
# @lcpr version=30204
#
# [1039] Minimum Score Triangulation of Polygon
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)
        @cache
        def f(i, j):
            if i + 1 >= j: # 邊數 j - i + 1 <= 2 不能構成三角形
                return 0
            res = float('inf')
            for k in range(i + 1, j):
                res = min(res, f(i, k) + f(k, j) + v[i] * v[k] * v[j])
            return res
        return f(0, n - 1)
    
class Solution2a:
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)
        f = [[0] * n for _ in range(n)]
        for ln in range(3, n + 1): # 枚舉長度
            for i in range(n - ln + 1): # 枚舉左端點
                j = i + ln - 1 # 右端點
                f[i][j] = float('inf')
                for k in range(i + 1, j): # 枚舉分界點
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + v[i] * v[k] * v[j])
        return f[0][n - 1]
    

class Solution2b:
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                f[i][j] = float('inf')
                for k in range(i + 1, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + v[i] * v[k] * v[j])
        return f[0][n - 1]
    
# class Solution(Solution1):
# class Solution(Solution2a):
class Solution(Solution2b):
    pass
# @lc code=end

sol = Solution()
print(sol.minScoreTriangulation([1,2,3])) # 6
print(sol.minScoreTriangulation([3,7,4,5])) # 144
print(sol.minScoreTriangulation([1,3,1,4,1,5])) # 13

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,7,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1,4,1,5]\n
# @lcpr case=end

#

