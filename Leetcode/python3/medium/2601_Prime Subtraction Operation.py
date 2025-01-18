#
# @lc app=leetcode id=2601 lang=python3
# @lcpr version=30204
#
# [2601] Prime Subtraction Operation
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAXN = 1000
is_prime = [True] * (MAXN + 1)
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, MAXN + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MAXN + 1, i):
            is_prime[j] = False

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pre = 0
        for x in nums:
            if x <= pre:
                return False
            idx = bisect_left(primes, x - pre) - 1
            pre = (x - primes[idx]) if idx >= 0 else x
        return True
# @lc code=end



#
# @lcpr case=start
# [4,9,6,10]\n
# @lcpr case=end

# @lcpr case=start
# [6,8,11,12]\n
# @lcpr case=end

# @lcpr case=start
# [5,8,3]\n
# @lcpr case=end

#

