#
# @lc app=leetcode id=518 lang=python3
# @lcpr version=30204
#
# [518] Coin Change II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    DP 先枚舉硬幣，再枚舉金額，就能使同種硬幣先被處理，進而確保不重複。
    
    例如當 coins = [2, 5]，x = 9 時，先枚舉硬幣再枚舉金額會是：
    - 2
    - 2 + 2
    - 2 + 2 + 2
    - 2 + 2 + 2 + 2
    - 5
    - 2 + 5
    - 2 + 2 + 5 (o)
    但先枚舉金額再枚舉硬幣會是：
    - 2
    - 2 + 2
    - 5
    - 2 + 2 + 2
    - 5 + 2
    - 2 + 5
    - 2 + 2 + 2 + 2
    - 5 + 2 + 2 (o)
    - 2 + 5 + 2 (o)
    - 2 + 2 + 5 (o)
"""
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]
# @lc code=end



#
# @lcpr case=start
# 5\n[1,2,5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[10]\n
# @lcpr case=end

#

