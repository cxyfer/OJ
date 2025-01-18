#
# @lc app=leetcode id=762 lang=python3
# @lcpr version=30202
#
# [762] Prime Number of Set Bits in Binary Representation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # return self.solve1(left, right)
        # return self.solve2(left, right)
        return self.solve3(left, right)
    def bit_count(self, n):
        res = 0
        while n:
            n &= n - 1 # 清除最低位的1
            res += 1
        return res
    def solve1(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2 or n % 2 == 0 and n != 2: # 先判斷是否為2的倍數
                return False
            for i in range(3, int(n ** 0.5) + 1, 2): # 之後只判斷是否為奇數的倍數
                if n % i == 0:
                    return False
            return True
        return sum(is_prime(x.bit_count()) for x in range(left, right + 1))
    def solve2(self, left: int, right: int) -> int:
        MAX_N = 20
        is_prime = [False, False] + [True] * (MAX_N - 2)
        for i in range(2, math.isqrt(MAX_N) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_N, i):
                    is_prime[j] = False
        return sum(is_prime[x.bit_count()] for x in range(left, right + 1))
    def solve3(self, left: int, right: int) -> int: # 範圍內的質數只有 2,3,5,7,11,13,17,19
        return sum(((1 << x.bit_count()) & 0b10100010100010101100) != 0 for x in range(left, right + 1))
# @lc code=end



#
# @lcpr case=start
# 6\n10\n
# @lcpr case=end

# @lcpr case=start
# 10\n15\n
# @lcpr case=end

#

