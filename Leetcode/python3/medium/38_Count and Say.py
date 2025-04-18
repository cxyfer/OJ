#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MX_N = 30
ans = [""] * (MX_N + 1)
ans[1] = "1"

def say(s):
    n = len(s)
    i = 0
    res = ""
    while (i < n):
        j = i
        while i < n and s[i] == s[j]:
            i += 1
        res += str(i - j) + s[j]
    return res

for n in range(2, MX_N + 1):
    ans[n] = say(ans[n-1])

class Solution:
    def countAndSay(self, n: int) -> str:
        return ans[n]
# @lc code=end

sol = Solution()
print(sol.countAndSay(4))
print(sol.countAndSay(1))