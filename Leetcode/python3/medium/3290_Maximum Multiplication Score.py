#
# @lc app=leetcode id=3290 lang=python3
# @lcpr version=30204
#
# [3290] Maximum Multiplication Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Variation of LCS
"""
# @lc code=start
class Solution1:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n:
                return 0
            if j == m:
                return float('-inf')
            return max(dfs(i, j + 1), dfs(i + 1, j + 1) + a[i] * b[j])
        return dfs(0, 0)

class Solution2a:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            if j < 0:
                return float('-inf')
            return max(dfs(i, j - 1), dfs(i - 1, j - 1) + a[i] * b[j])
        return dfs(n - 1, m - 1)

class Solution2b:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            f[i][0] = float('-inf')
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = max(f[i][j - 1], f[i - 1][j - 1] + a[i - 1] * b[j - 1])
        return f[n][m]

class Solution2c:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        f = [[0] * (m + 1) for _ in range(2)]
        for i in range(1, n + 1):
            cur, pre = i & 1, (i - 1) & 1
            f[cur][0] = float('-inf')
            for j in range(1, m + 1):
                f[cur][j] = max(f[cur][j - 1], f[pre][j - 1] + a[i - 1] * b[j - 1])
        return f[n & 1][m]

# Solution = Solution1
# Solution = Solution2a
# Solution = Solution2b
Solution = Solution2c
# @lc code=end

sol = Solution()
print(sol.maxScore([3,2,5,6], [2,-6,4,-5,-3,2,-7])) # 26
print(sol.maxScore([-1,4,5,-2], [-5,-1,-3,-2,-4])) # -1

#
# @lcpr case=start
# [3,2,5,6]\n[2,-6,4,-5,-3,2,-7]\n
# @lcpr case=end

# @lcpr case=start
# [-1,4,5,-2]\n[-5,-1,-3,-2,-4]\n
# @lcpr case=end

#

