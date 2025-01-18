#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from preImport import *
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0]*i for i in range(1,numRows+1)]
        ans[0][0] = 1
        for i in range(1, numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
        return ans
# @lc code=end

