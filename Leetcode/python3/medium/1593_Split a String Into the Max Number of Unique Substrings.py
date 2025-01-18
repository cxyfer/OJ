#
# @lc app=leetcode id=1593 lang=python3
# @lcpr version=30204
#
# [1593] Split a String Into the Max Number of Unique Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        path = set()
        def dfs(i: int) -> int:
            if i == n:
                return len(path)
            res = 0
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub not in path:
                    path.add(sub)
                    res = max(res, dfs(j))
                    path.remove(sub)
            return res
        return dfs(0)
# @lc code=end



#
# @lcpr case=start
# "ababccc"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

#

