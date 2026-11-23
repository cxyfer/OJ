#
# @lc app=leetcode id=1352 lang=python3
# @lcpr version=30204
#
# [1352] Product of the Last K Numbers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = int(1e2 + 5)

# prime
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False
primes = [x for x in range(2, MAX_N) if is_prime[x]]

M = len(primes)


def prime_factorization(x: int) -> list[int]:
    E = [0] * M
    if x != 0:
        for i, p in enumerate(primes):
            while x % p == 0:
                E[i] += 1
                x //= p
    return E


class ProductOfNumbers1:
    def __init__(self):
        self.preProd = [[0] * M]
        self.preZero = [0]

    def add(self, num: int) -> None:
        self.preZero.append(self.preZero[-1] + (num == 0))
        self.preProd.append([self.preProd[-1][i] + e for i, e in enumerate(prime_factorization(num))])

    def getProduct(self, k: int) -> int:
        if self.preZero[-1] - self.preZero[-1 - k] > 0:
            return 0
        ans = 1
        for i, p in enumerate(primes):
            e = self.preProd[-1][i] - self.preProd[-1 - k][i]
            ans *= pow(p, e)
        return ans


class ProductOfNumbers2:
    def __init__(self):
        self.preProd = [1]
        self.lastZero = -1

    def add(self, num: int) -> None:
        if num != 0:
            self.preProd.append(self.preProd[-1] * num)
        else:
            self.preProd.append(1)
            self.lastZero = len(self.preProd) - 1

    def getProduct(self, k: int) -> int:
        if len(self.preProd) - 1 - k < self.lastZero:
            return 0
        return self.preProd[-1] // self.preProd[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# ProductOfNumbers = ProductOfNumbers1
ProductOfNumbers = ProductOfNumbers2
# @lc code=end
