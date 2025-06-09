#
# @lc app=leetcode id=3577 lang=python3
#
# [3577] Count the Number of Computer Unlocking Permutations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
N = int(1e5)
MOD = int(1e9+7)
fact = [1] * (N + 1)
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i % MOD

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        mn = min(complexity)
        if mn != complexity[0] or complexity.count(mn) > 1:
            return 0
        return fact[n - 1]
# @lc code=end

