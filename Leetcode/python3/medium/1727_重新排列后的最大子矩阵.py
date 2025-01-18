#
# @lc app=leetcode.cn id=1727 lang=python3
#
# [1727] 重新排列后的最大子矩阵
#
from preImport import *
# @lc code=start
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        up = [[0] * n for _ in range(m)] # up[i][j] = (i,j) 上方有幾個 1 (包含自己)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0:
                        up[i][j] = 1
                    else:
                        up[i][j] = up[i-1][j] + 1
        # print(up)
        ans = 0
        for i in range(m): # 枚舉最大矩形的底部位置 i 
            buf = sorted(up[i])
            for j in range(n):
                h = buf[j] # 高度
                w = n - j # 寬度
                ans = max(ans, h * w)
        return ans 
# @lc code=end

sol = Solution()

print(sol.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]])) # 4
print(sol.largestSubmatrix([[1,0,1,0,1]])) # 3
print(sol.largestSubmatrix([[1,1,0],[1,0,1]])) # 2
