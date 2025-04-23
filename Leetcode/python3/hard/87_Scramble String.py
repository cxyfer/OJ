#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
@cache
def dfs(x: str, y: str) -> bool:
    if x == y:
        return True
    if sorted(x) != sorted(y):  # 剪枝
        return False

    n = len(x)
    for i in range(1, n):
        if dfs(x[:i], y[:i]) and dfs(x[i:], y[i:]):
            return True
        if dfs(x[:i], y[-i:]) and dfs(x[i:], y[:-i]):
            return True
    return False

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return dfs(s1, s2)
# @lc code=end

