#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        n = len(s)
        ans = ["" for i in range(numRows)]
        idx = 0
        dir = 1
        for ch in s:
            ans[idx] += ch
            if idx == 0:
                dir = 1
            elif idx == numRows - 1:
                dir = -1
            idx += dir
        return "".join(ans)
# @lc code=end
print(Solution().convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR
print(Solution().convert("PAYPALISHIRING", 4)) # PINALSIGYAHRPI
print(Solution().convert("A", 1)) # A
print(Solution().convert("AB", 1)) # AB