#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        num = 0
        cur = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                st.append((num, cur))
                num = 0
                cur = ""
            elif ch == ']':
                n, t = st.pop()
                cur = t + cur * n
            else:
                cur += ch
        return cur
# @lc code=end

sol = Solution()
print(sol.decodeString("3[a]2[bc]")) # "aaabcbc"

