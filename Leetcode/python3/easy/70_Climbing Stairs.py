#
# @lc app=leetcode id=70 lang=python3
# @lcpr version=30201
#
# [70] Climbing Stairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Dynamic Programming
            O(n)
        2. Matrix Exponentiation
            O(logn)
        3. Fibonacci Formula
            O(1)
    """
    def climbStairs(self, n: int) -> int:
        # return self.solve1a(n)
        # return self.solve1b(n)
        # return self.solve2(n)
        return self.solve3(n)
    def solve1a(self, n: int) -> int: # O(n) space
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    def solve1b(self, n: int) -> int: # O(1) space
        p, q, r = 0, 0, 1
        for _ in range(n):
            p, q = q, r
            r = p + q
        return r
    def solve2(self, n: int) -> int:
        matrix = [[1, 1], [1, 0]]
        def matrix_mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            x, y, z = len(a), len(b), len(b[0])
            res = [[0] * z for _ in range(x)]
            for i in range(x):
                for j in range(z):
                    c = 0
                    for k in range(y):
                        c += a[i][k] * b[k][j]
                    res[i][j] = c
            return res
        def matrix_pow(m: List[List[int]], n: int) -> List[List[int]]:
            res = [[1, 0], [0, 1]]
            while n:
                if n & 1:
                    res = matrix_mul(res, m)
                m = matrix_mul(m, m)
                n >>= 1
            return res
        return matrix_pow(matrix, n)[0][0]
    def solve3(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n+1) - math.pow((1 - sqrt5) / 2, n+1)
        return int(fibn / sqrt5)
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

