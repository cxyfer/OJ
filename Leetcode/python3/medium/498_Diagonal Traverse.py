#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. My Solution
2. Template from 0x3f
"""
# @lc code=start
class Solution1:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        x, y = 0, 0
        ans = []
        for _ in range(m * n):
            ans.append(mat[x][y])
            if (x + y) & 1 == 0:
                if y == n - 1:
                    x += 1
                elif x == 0: 
                    y += 1
                else:
                    x -= 1
                    y += 1
            else:
                if x == m - 1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1
        return ans

class Solution2:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        for k in range(m + n - 1):  # 枚舉 x + y 的值
            min_j = max(k - m + 1, 0)
            max_j = min(k, n - 1)
            if k & 1 == 0:
                for j in range(min_j, max_j + 1):
                    ans.append(mat[k - j][j])
            else:
                for j in range(max_j, min_j - 1, -1):
                    ans.append(mat[k - j][j])
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

