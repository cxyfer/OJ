#
# @lc app=leetcode id=3233 lang=python3
# @lcpr version=30204
#
# [3233] Find the Count of Numbers Which Are Not Special
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAXN = int(1e9 + 5)
MAXN_SQRT = math.isqrt(MAXN)
is_prime = [True] * (MAXN_SQRT + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, MAXN_SQRT + 1):
    if is_prime[i]:
        for j in range(i * i, MAXN_SQRT + 1, i):
            is_prime[j] = False
nums = [i * i for i in range(2, MAXN_SQRT + 1) if is_prime[i]]
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        return r - l + 1 - (bisect_right(nums, r) - bisect_left(nums, l))
# @lc code=end

sol = Solution()
print(sol.nonSpecialCount(5, 7)) # 3
print(sol.nonSpecialCount(4, 16)) # 11

#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 4\n16\n
# @lcpr case=end

#

