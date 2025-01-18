#
# @lc app=leetcode id=204 lang=python3
# @lcpr version=30201
#
# [204] Count Primes
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)
# @lc code=end

sol = Solution()
print(sol.countPrimes(10)) # 4
print(sol.countPrimes(3)) # 0


#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

