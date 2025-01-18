#
# @lc app=leetcode id=3259 lang=python3
# @lcpr version=30204
#
# [3259] Maximum Energy Boost From Two Drinks
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)

        @cache
        def f(i: int, j: int) -> int:
            if i >= n:
                return 0
            drink = [energyDrinkA[i], energyDrinkB[i]]
            return max(drink[j] + f(i + 1, j), f(i + 1, j ^ 1))

        return max(f(0, 0), f(0, -1))
# @lc code=end

s = Solution()
print(s.maxEnergyBoost([1,3,1], [3,1,1])) # 5
print(s.maxEnergyBoost([4,1,1], [1,1,3])) # 7
print(s.maxEnergyBoost([3,3,3], [3,4,6])) # 13

#
# @lcpr case=start
# [1,3,1]\n[3,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,1]\n[1,1,3]\n
# @lcpr case=end

#

