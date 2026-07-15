#
# @lc app=leetcode id=3658 lang=python3
#
# [3658] GCD of Odd and Even Sums
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = (1 + 2 * n - 1) * n // 2
        sum_even = (2 + 2 * n) * n // 2
        return math.gcd(sum_odd, sum_even)


class Solution2:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # gcd(n * n, n * (n + 1)) = n * gcd(n, n + 1) = n
        return n


# Solution = Solution1
Solution = Solution2
# @lc code=end

