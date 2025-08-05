#
# @lc app=leetcode id=3477 lang=python3
#
# [3477] Fruits Into Baskets II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        ans = 0
        for fruit in fruits:
            for i in range(n):
                if baskets[i] >= fruit:
                    baskets[i] = -1
                    break
            else:
                ans += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.numOfUnplacedFruits([4,2,5], [3,5,4]))  # 1
print(sol.numOfUnplacedFruits([3,6,1], [6,4,7]))  # 0