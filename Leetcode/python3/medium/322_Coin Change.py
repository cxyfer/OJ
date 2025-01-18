#
# @lc app=leetcode id=322 lang=python3
# @lcpr version=30204
#
# [322] Coin Change
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Dynamic Programming
        dp[i] 表示湊成 i 所需的最少硬幣數量
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i < c:
                    break
                dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1   
# @lc code=end



#
# @lcpr case=start
# [1,2,5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

