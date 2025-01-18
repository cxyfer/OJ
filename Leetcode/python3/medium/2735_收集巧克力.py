#
# @lc app=leetcode.cn id=2735 lang=python3
#
# [2735] 收集巧克力
#
from preImport import *
# @lc code=start
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = [x * i for i in range(n)] # ans[k] 表示操作 k 次時，收集所有巧克力的最小總花費
        for i, cost in enumerate(nums): # 枚舉每種巧克力，計算對操作 k 次的總花費的貢獻
            for k in range(n): # 操作次數
                cost = min(cost, nums[(i+k)%n]) # 第i種巧克力，操作 0~k 次的最小花費
                ans[k] += cost # 對操作 k 次的總花費的貢獻
        return min(ans)

# @lc code=end
sol = Solution()
print(sol.minCost([20,1,15],5)) # 13
print(sol.minCost([1,2,3],4)) # 6
