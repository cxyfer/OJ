#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        # return min(sum([(ch == '1') if i % 2 == 0 else (ch == '0') for i, ch in enumerate(s)]), sum([(ch == '0') if i % 2 == 0 else (ch == '1') for i, ch in enumerate(s)]))
        ans1 = ans2 = 0
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch == '1':
                    ans1 += 1
                else:
                    ans2 += 1
            else:
                if ch == '0':
                    ans1 += 1
                else:
                    ans2 += 1
        return min(ans1, ans2)
# @lc code=end

