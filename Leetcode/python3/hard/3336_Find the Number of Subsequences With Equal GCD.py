#
# @lc app=leetcode id=3336 lang=python3
# @lcpr version=30204
#
# [3336] Find the Number of Subsequences With Equal GCD
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

gcdCache = [[0] * 201 for _ in range(201)]
for i in range(201):
    for j in range(i, 201):
        gcdCache[i][j] = gcdCache[j][i] = math.gcd(i, j)
gcd = lambda x, y: gcdCache[x][y]

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        @cache
        def f(i: int, g1: int, g2: int) -> int:
            if i == n:
                return 1 if g1 == g2 else 0
            res1 = f(i + 1, g1, g2)
            res2 = f(i + 1, gcd(g1, nums[i]), g2)
            res3 = f(i + 1, g1, gcd(g2, nums[i]))
            return (res1 + res2 + res3) % MOD
        return (f(0, 0, 0) - 1) % MOD
# @lc code=end

sol = Solution()
print(sol.subsequencePairCount([1,2,3,4])) # 10
print(sol.subsequencePairCount([10,20,30])) # 2
print(sol.subsequencePairCount([1,1,1,1])) #50


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [10,20,30]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#

