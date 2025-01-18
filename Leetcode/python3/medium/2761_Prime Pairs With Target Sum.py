#
# @lc app=leetcode id=2761 lang=python3
# @lcpr version=30202
#
# [2761] Prime Pairs With Target Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

MAX_N = int(5e6+5)
is_prime = [False] * 2 + [True] * (MAX_N - 2) # Sieve of Eratosthenes
for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans = []
        if is_prime[n - 2]: # 2 is the only even prime
            ans.append([2, n - 2])
        for i in range(3, n//2+1, 2): # only odd numbers can be prime, except 2
            if is_prime[i] and is_prime[n - i]:
                ans.append([i, n - i])
        return ans
# @lc code=end



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

