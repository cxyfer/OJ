#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
from preImport import *
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            ans = [1] + [ans[i] + ans[i+1] for i in range(len(ans)-1)] + [1]
        return ans
# @lc code=end
sol = Solution()
print(sol.getRow(3)) # [1,3,3,1]
