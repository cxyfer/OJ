#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def fib(self, n: int) -> int:
        @cache
        def dfs(n: int) -> int:
            if n <= 1:
                return n
            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)


class Solution2:
    def fib(self, n: int) -> int:
        f = [0] * (max(n, 1) + 1)
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


class Solution3:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f0, f1 = 0, 1
        for _ in range(2, n + 1):
            f0, f1 = f1, f0 + f1
        return f1


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

