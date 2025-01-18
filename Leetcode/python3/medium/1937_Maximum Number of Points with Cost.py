#
# @lc app=leetcode id=1937 lang=python3
# @lcpr version=30204
#
# [1937] Maximum Number of Points with Cost
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. O(mn * n) -> TLE
    2. O(mn) -> AC
"""
class Solution1:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        def dfs(i, j): # i is the row, j is the previous column
            if i == m: return 0
            res = -float("inf")
            for j2 in range(n):
                res = max(res, points[i][j2] - abs(j-j2) + dfs(i+1, j2))
            return res

        ans = -float("inf")
        for j in range(n):
            ans = max(ans, points[0][j] + dfs(1, j))
        return ans

class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
        for i in range(1, m):
            pre, suf = float("-inf"), float("-inf")  # 前後綴的最大值
            for j in range(n):
                pre = max(pre, dp[i-1][j] + j)
                dp[i][j] = max(dp[i][j], points[i][j] - j + pre) # type: ignore
            for j in range(n-1, -1, -1):
                suf = max(suf, dp[i-1][j] - j)
                dp[i][j] = max(dp[i][j], points[i][j] + j + suf) # type: ignore
        return max(dp[m-1])

# class Solution(Solution1): 
class Solution(Solution2):
    pass
# @lc code=end

[[1,5],[3,2],[4,2]]
sol = Solution()
print(sol.maxPoints([[1,5],[3,2],[4,2]])) # 11

#
# @lcpr case=start
# [[1,2,3],[1,5,1],[3,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5],[2,3],[4,2]]\n
# @lcpr case=end

#

