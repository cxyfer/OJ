#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = []
        def dfs(i):
            if i == n:
                if len(path) == 4:
                    ans.append(".".join(path))
                return
            if len(path) == 4:
                return
            if s[i] == "0":
                path.append(s[i])
                dfs(i + 1)
                path.pop()
                return
            
            for j in range(i, n):
                if int(s[i:j+1]) > 255:
                    break
                path.append(s[i:j+1])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return ans
# @lc code=end

