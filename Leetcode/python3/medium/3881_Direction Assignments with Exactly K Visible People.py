#
# @lc app=leetcode id=3881 lang=python3
#
# [3881] Direction Assignments with Exactly K Visible People
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = int(1e9 + 7)
MAX_N = int(1e5 + 5)

fact = [1] * MAX_N
for i in range(1, MAX_N):
    fact[i] = fact[i - 1] * i % MOD
invf = [-1] * MAX_N
invf[-1] = pow(fact[-1], -1, MOD)
for i in range(MAX_N - 1, 0, -1):
    invf[i - 1] = invf[i] * i % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * invf[k] * invf[n - k] % MOD

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        return comb(n - 1, k) * 2 % MOD
        # ans = 0
        # for l in range(k + 1):
        #     ans += comb(pos, l) * comb(n - pos - 1, k - l) % MOD
        # return ans * 2 % MOD
# @lc code=end

