#
# @lc app=leetcode id=3115 lang=python3
# @lcpr version=30202
#
# [3115] Maximum Prime Difference
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = 105
is_prime = [False, False] + [True] * (MAX_N - 2)
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        # prime = [i for i, x in enumerate(nums) if is_prime[x]]
        # if len(prime) < 2:
        #     return 0
        # return prime[-1] - prime[0]
        i = 0
        while not is_prime[nums[i]]:
            i += 1
        j = len(nums) - 1
        while not is_prime[nums[j]]:
            j -= 1
        return j - i
# @lc code=end



#
# @lcpr case=start
# [4,2,9,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,8,2,8]\n
# @lcpr case=end

#

