#
# @lc app=leetcode.cn id=1599 lang=python3
#
# [1599] 经营摩天轮的最大利润
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. 模擬
    """
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)
        ans = -1 # 最大利潤所需輪數
        mx = cur = 0 # 最大利潤, 當前利潤
        wait = 0 # 等待人數
        i = 0
        while wait or i < n:
            if i < n:
                wait += customers[i]
            cur += min(4, wait) * boardingCost - runningCost
            wait -= min(4, wait)
            if cur > mx: # 更新最大利潤
                mx = cur
                ans = i + 1
            i += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.minOperationsMaxProfit([8,3],5,6)) # 3
print(sol.minOperationsMaxProfit([10,9,6],6,4)) # 7
print(sol.minOperationsMaxProfit([3,4,0,5,1],1,92)) # -1