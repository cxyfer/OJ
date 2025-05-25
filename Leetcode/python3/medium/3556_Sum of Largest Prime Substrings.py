#
# @lc app=leetcode id=3556 lang=python3
#
# [3556] Sum of Largest Prime Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
def isPrime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        n = len(s)
        st = set()
        for i in range(n):
            for j in range(i, n):
                x = int(s[i:j + 1])
                if isPrime(x):
                    st.add(x)
        return sum(sorted(st, reverse=True)[:3])
# @lc code=end

sol = Solution()
print(sol.sumOfLargestPrimes("12234"))
print(sol.sumOfLargestPrimes("111"))