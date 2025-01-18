# @algorithm @lc id=1845 lang=python3 
# @title largest-submatrix-with-rearrangements


from en.Python3.mod.preImport import *
# @test([[0,0,1],[1,1,1],[1,0,1]])=4
# @test([[1,0,1,0,1]])=3
# @test([[1,1,0],[1,0,1]])=2
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