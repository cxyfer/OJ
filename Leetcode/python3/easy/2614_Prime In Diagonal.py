#
# @lc app=leetcode id=2614 lang=python3
# @lcpr version=30202
#
# [2614] Prime In Diagonal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAXN = int(4e6) + 5
is_prime = [True] * MAXN
is_prime[0] = is_prime[1] = False
for i in range(2, MAXN):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = False
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        ans = 0
        for i, row in enumerate(nums):
            for x in [row[i], row[n-1-i]]:
                if is_prime[x]:
                    ans = max(ans, x)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[5,6,7],[9,10,11]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,17,7],[9,11,10]]\n
# @lcpr case=end

#

