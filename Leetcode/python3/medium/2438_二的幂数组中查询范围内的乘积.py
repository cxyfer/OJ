#
# @lc app=leetcode.cn id=2438 lang=python3
#
# [2438] 二的幂数组中查询范围内的乘积
#
from preImport import *
# @lc code=start
MOD = 10 ** 9 + 7
pow2 = [1] # 2^i % MOD
for i in range(500):
    pow2.append(pow2[-1] * 2 % MOD)

class Solution:
    """
        1. Prefix Sum + Exponentiation by Squaring / Preprocessing
        2. Prefix Sum + Inverse

        Ref: https://leetcode.cn/problems/range-product-queries-of-powers/solutions/2453873/yi-ti-duo-jie-bu-chong-ling-shen-bzhan-s-20vb/
    """
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        return self.solve1(n, queries)
        # return self.solve2(n, queries)
    def solve1(self, n: int, queries: List[List[int]]) -> List[int]:
        s = [0] # prefix sum of exponents of 2
        while n:
            lb = n & -n # lowest bit
            s.append(s[-1] + lb.bit_length() - 1) 
            n ^= lb # remove lowest bit
        # return [pow(2, s[r + 1] - s[l], MOD) for l, r in queries] # Exponentiation by Squaring
        return [pow2[s[r + 1] - s[l]] for l, r in queries] # Preprocessing
    def solve2(self, n: int, queries: List[List[int]]) -> List[int]:
        s = [1] # prefix sum
        while n:
            lb = n & -n # lowest bit
            s.append(s[-1] * lb)
            n ^= lb # remove lowest bit
        inv = [pow(x, MOD - 2, MOD) for x in s] # inverse
        return [s[r + 1] * inv[l] % MOD for l, r in queries]
# @lc code=end
sol = Solution()
print(sol.productQueries(15,[[0,1],[2,2],[0,3]])) # [2,4,64]
print(sol.productQueries(2,[[0,0]])) # [2]