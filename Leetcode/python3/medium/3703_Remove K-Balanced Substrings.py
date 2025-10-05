#
# @lc app=leetcode id=3703 lang=python3
#
# [3703] Remove K-Balanced Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        st = []
        for ch in s:
            if st and st[-1][0] == ch:
                st[-1][1] += 1
            else:
                st.append([ch, 1])
            if len(st) > 1 and st[-1][0] == ')' and st[-1][1] == k and st[-2][1] >= k:
                st.pop()
                st[-1][1] -= k
                if st[-1][1] == 0:
                    st.pop()
        return ''.join(ch * cnt for ch, cnt in st)
# @lc code=end
sol = Solution()
print(sol.removeSubstring(")(", 1))  # ")("
print(sol.removeSubstring("(()(()(()))((()", 2))  # "(()((()"