#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for ch in s:
            if 'A' <= ch <= 'Z':
                ans.append(chr(ord(ch) + 32))
            else:
                ans.append(ch)
        return ''.join(ans)
# @lc code=end

