#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        # return format(x + y, 'b')
        while y:
            c = ((x & y) << 1) # Carry bit array
            x = x ^ y # Sum bit array
            y = c # Continue until no carry bit
        return format(x, 'b') # Convert to binary string
# @lc code=end

