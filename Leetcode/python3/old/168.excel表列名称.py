#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ''
        while n > 0:
            n -= 1
            ans = chr((n) % 26 + ord('A')) + ans
            n //= 26
        return ans
# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(1)) # "A"
    print(sol.convertToTitle(701)) # "ZY"
