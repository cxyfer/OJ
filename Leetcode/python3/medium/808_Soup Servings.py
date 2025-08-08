#
# @lc app=leetcode id=808 lang=python3
#
# [808] Soup Servings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
@cache
def dfs(a, b):
    if a <= 0 and b <= 0:
        return 0.5
    if a <= 0:
        return 1.0
    if b <= 0:
        return 0.0
    return (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b - 50) + dfs(a - 25, b - 75)) / 4

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        return dfs(n, n)
# @lc code=end

