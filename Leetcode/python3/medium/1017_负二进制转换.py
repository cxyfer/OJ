#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#
from preImport import *
# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        ans = ""
        while n:
            q, r = divmod(n, -2)
            if r < 0:
                q += 1
                r += 2
            ans += str(r)
            n = q
        return ans[::-1] if ans else "0"
# @lc code=end

