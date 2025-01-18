#
# @lc app=leetcode id=1449 lang=python3
# @lcpr version=30204
#
# [1449] Form Largest Integer With Digits That Add up to Target
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # dp[i] 表示成本為 i 所能獲得的最大位數
        dp = [-1] * (target + 1)
        dp[0] = 0
        for i in range(1, target + 1):
            for j in range(len(cost)):
                if i >= cost[j] and dp[i - cost[j]] != -1:
                    dp[i] = max(dp[i], dp[i - cost[j]] + 1)
        if dp[target] == -1:
            return "0"
        # 回過頭來找最大數字
        # 如果當前的 cost[i] 可以被使用，且使用後的 dp[target - cost[i]] 為前述計算時的轉移來源
        # 則當前數字 i + 1 是答案的一部分，根據貪心原則，把較大的數字放在前面
        ans = ""
        for i in range(len(cost) - 1, -1, -1):
            while target >= cost[i] and dp[target - cost[i]] == dp[target] - 1:
                ans += str(i + 1)
                target -= cost[i]
        return ans
# @lc code=end

sol = Solution()
print(sol.largestNumber([4,3,2,5,6,7,2,5,5], 9))

#
# @lcpr case=start
# [4,3,2,5,6,7,2,5,5]\n9\n
# @lcpr case=end

# @lcpr case=start
# [7,6,5,5,5,6,8,7,8]\n12\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,2,4,6,4,4,4]\n5\n
# @lcpr case=end

#

