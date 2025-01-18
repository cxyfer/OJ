#
# @lc app=leetcode id=1492 lang=python3
# @lcpr version=30201
#
# [1492] The kth Factor of n
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Brute force
            - Time: O(n)
            - Space: O(n) / O(1)
        2. Optimized brute force
            - Time: O(sqrt(n))
            - Space: O(sqrt(n)) / O(1)
    """
    def kthFactor(self, n: int, k: int) -> int:
        # return self.solve1a(n, k)
        # return self.solve1b(n, k)
        # return self.solve2a(n, k)
        return self.solve2b(n, k)
    def solve1a(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        return factors[k-1] if k <= len(factors) else -1
    def solve1b(self, n: int, k: int) -> int:
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1
    def solve2a(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                factors.append(i)
        m = len(factors)
        if factors[m-1] ** 2 == n:
            m -= 1
        for i in range(m-1, -1, -1):
            factors.append(n // factors[i])
        return factors[k-1] if k <= len(factors) else -1
    def solve2b(self, n: int, k: int) -> int:
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        if i ** 2 == n:
            i -= 1
        for j in range(i, 0, -1):
            if n % j == 0:
                k -= 1
                if k == 0:
                    return n // j
        return -1
# @lc code=end

sol = Solution()
# print(sol.kthFactor(12, 3)) # 3
# print(sol.kthFactor(7, 2)) # 7
print(sol.kthFactor(2, 2)) # 2



#
# @lcpr case=start
# 12\n3\n
# @lcpr case=end

# @lcpr case=start
# 7\n2\n
# @lcpr case=end

# @lcpr case=start
# 4\n4\n
# @lcpr case=end

#

