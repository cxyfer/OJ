#
# @lc app=leetcode.cn id=2390 lang=python3
#
# [2390] 从字符串中移除星号
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            if c == '*':
                if st: st.pop()
            else:
                st.append(c)
        return ''.join(st)
# @lc code=end

