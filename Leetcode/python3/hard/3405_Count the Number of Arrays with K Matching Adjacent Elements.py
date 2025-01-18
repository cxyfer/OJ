#
# @lc app=leetcode id=3405 lang=python3
# @lcpr version=30204
#
# [3405] Count the Number of Arrays with K Matching Adjacent Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 10**9 + 7
MAXN = int(1e5 + 5)

fact = [1] * (MAXN + 1)
invf = [1] * (MAXN + 1)
for i in range(2, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD
invf[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
for i in range(MAXN - 1, 0, -1):
    invf[i] = (invf[i+1] * (i+1)) % MOD

def comb(n, r):
    return (fact[n] * invf[r] % MOD) * invf[n-r] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb(n - 1, k) * m * pow(m - 1, (n - 1) - k, MOD) % MOD
# @lc code=end



#
# @lcpr case=start
# 3\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n2\n2\n
# @lcpr case=end

# @lcpr case=start
# 5\n2\n0\n
# @lcpr case=end

#

