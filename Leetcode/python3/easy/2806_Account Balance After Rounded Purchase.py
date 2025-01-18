#
# @lc app=leetcode id=2806 lang=python3
# @lcpr version=30203
#
# [2806] Account Balance After Rounded Purchase
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # return self.solve1(purchaseAmount)
        return self.solve2(purchaseAmount)
    def solve1(self, purchaseAmount: int) -> int:
        x = purchaseAmount // 10
        cost1, cost2 = x * 10, (x + 1) * 10
        if purchaseAmount - cost1 < cost2 - purchaseAmount: # 較小的 roundedAmount 比較接近 purchaseAmount
            return 100 - cost1
        else: # 較大的 roundedAmount 比較接近 purchaseAmount 或 兩者一樣接近
            return 100 - cost2
    def solve2(self, purchaseAmount: int) -> int:
        cost = (purchaseAmount + 5) // 10 * 10
        return 100 - cost
# @lc code=end



#
# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 15\n
# @lcpr case=end

#

