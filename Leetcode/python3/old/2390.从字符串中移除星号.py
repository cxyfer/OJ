#
# @lc app=leetcode.cn id=2390 lang=python3
#
# [2390] 从字符串中移除星号
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        if s.count('*') >= (len(s)+1) // 2:
            return ''
        st = []
        for c in s:
            if c == '*':
                st.pop()
            else:
                st.append(c)
        return ''.join(st)
# @lc code=end

