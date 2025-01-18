#
# @lc app=leetcode id=2381 lang=python3
# @lcpr version=30204
#
# [2381] Shifting Letters II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0] * (n + 1)
        for l, r, k in shifts:
            delta = 1 if k == 1 else -1
            d[l] += delta
            d[r+1] -= delta
        
        for i in range(1, n):
            d[i] += d[i-1]
        
        ans = [""] * n
        for i, (ch, d_i) in enumerate(zip(s, d)):
            ans[i] = chr(ord('a') + (ord(ch) - ord('a') + d_i) % 26)
        return ''.join(ans)
# @lc code=end



#
# @lcpr case=start
# "abc"\n[[0,1,0],[1,2,1],[0,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# "dztz"\n[[0,0,0],[1,1,1]]\n
# @lcpr case=end

#

