#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        st = []
        invalid = [False] * n
        for idx, ch in enumerate(s):
            if ch == '(':
                st.append(idx)
                invalid[idx] = True # 標記該下標的括號為無效
            elif ch == ')':
                if st:
                    invalid[st.pop()] = False # 取消標記
                else:
                    invalid[idx] = True # 標記該下標的括號為無效
        ans = [ch for idx, ch in enumerate(s) if not invalid[idx]]
        return ''.join(ans)
# @lc code=end

