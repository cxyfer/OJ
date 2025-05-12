#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])

        def check(grid):
            s = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + grid[i - 1][j - 1]

            if m == 1:
                for i in range(n):
                    if s[i + 1][m] == s[n][m] - s[i + 1][m]:
                        return True
                for i in range(1, n - 1):
                    if s[i + 1][m] - grid[i][0] == s[n][m] - s[i + 1][m]:
                        return True
                for i in range(1, n):
                    if s[i + 1][m] - grid[0][0] == s[n][m] - s[i + 1][m]:
                        return True
                return False
            
            if n == 1:
                for j in range(m):
                    if s[n][j + 1] == s[n][m] - s[n][j + 1]:
                        return True
                for j in range(1, m - 1):
                    if s[n][j + 1] - grid[0][j] == s[n][m] - s[n][j + 1]:
                        return True
                for j in range(1, m):
                    if s[n][j + 1] - grid[0][0] == s[n][m] - s[n][j + 1]:
                        return True
                return False

            st = set()
            for i in range(n):
                if i == 0:
                    st.add(grid[i][0])
                    st.add(grid[i][m - 1])
                else:
                    if i == 1:
                        for j in range(m):
                            st.add(grid[0][j])
                    for j in range(m):
                        st.add(grid[i][j])
                if 2 * s[i + 1][m] - s[n][m] in st:
                    return True
                if s[i + 1][m] == s[n][m] - s[i + 1][m]:
                    return True

            st = set()
            for j in range(m):
                if j == 0:
                    st.add(grid[0][j])
                    st.add(grid[n - 1][j])
                else:
                    if j == 1:
                        for i in range(n):
                            st.add(grid[i][0])
                    for i in range(n):
                        st.add(grid[i][j])
                # L = s[n][j + 1] - x
                # R = s[n][m] - s[n][j + 1]
                if 2 * s[n][j + 1] - s[n][m] in st:
                    return True
                if s[n][j + 1] == s[n][m] - s[n][j + 1]:
                    return True
            return False
        ans = check(grid)
        grid.reverse()
        for i in range(n):
            grid[i].reverse()
        ans |= check(grid)
        return ans
# @lc code=end

sol = Solution()
print(sol.canPartitionGrid([[1,2],[3,4]])) # true
print(sol.canPartitionGrid([[25372],[100000],[100000]])) # true