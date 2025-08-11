#
# @lc app=leetcode id=2438 lang=python3
#
# [2438] Range Product Queries of Powers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Prefix Sum + Exponentiation by Squaring / Preprocessing
2. Prefix Sum + Modular multiplicative inverse

Ref: https://leetcode.cn/problems/range-product-queries-of-powers/solutions/2453873/yi-ti-duo-jie-bu-chong-ling-shen-bzhan-s-20vb/
"""
# @lc code=start
MOD = int(1e9 + 7)

class Solution1a:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        s = [0]
        while n:
            lb = n & -n
            s.append(s[-1] + lb.bit_length() - 1)
            n ^= lb
        return [pow(2, s[r + 1] - s[l], MOD) for l, r in queries]

pow2 = [1]
for i in range(500):
    pow2.append(pow2[-1] * 2 % MOD)

class Solution1b:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        s = [0]
        while n:
            lb = n & -n
            s.append(s[-1] + lb.bit_length() - 1)
            n ^= lb
        return [pow2[s[r + 1] - s[l]] for l, r in queries]

class Solution2:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = int(1e9 + 7)
        s = [1]
        while n:
            lb = n & -n
            s.append(s[-1] * lb % MOD)
            n ^= lb
        inv = [pow(x, MOD - 2, MOD) for x in s]
        return [(s[r + 1] * inv[l]) % MOD for l, r in queries]

# Solution = Solution1a
# Solution = Solution1b
Solution = Solution2
# @lc code=end
