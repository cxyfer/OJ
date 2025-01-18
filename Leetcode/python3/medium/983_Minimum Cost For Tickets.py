#
# @lc app=leetcode id=983 lang=python3
# @lcpr version=30204
#
# [983] Minimum Cost For Tickets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 記憶化搜索 O(D)
2. 基於值域的迭代 O(D)
3. 基於日期，三指標 O(n)
"""
# @lc code=start
class Solution1:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        first_day, last_day = days[0], days[-1]

        @cache
        def dfs(i): # dfs(i) 表示從第 i 天開始旅行的最小花費
            if i > last_day:
                return 0
            if i in days_set: # 第 i 天需要買票，則比較三種買票方案的花費，取最小值
                return min(costs[0] + dfs(i + 1), costs[1] + dfs(i + 7), costs[2] + dfs(i + 30))
            else: # 第 i 天不需要買票，可以跳過
                return dfs(i + 1)
            
        return dfs(first_day)
    
class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        first_day, last_day = days[0], days[-1]
        # dp[i] 表示從第 i 天開始旅行的最小花費
        dp = [0] * (last_day + 31) # 多開 30 天，避免索引越界
        for i in range(last_day, first_day - 1, -1):
            if i in days_set:
                dp[i] = min(costs[0] + dp[i + 1], costs[1] + dp[i + 7], costs[2] + dp[i + 30])
            else:
                dp[i] = dp[i + 1]
        return dp[first_day]
 
class Solution3:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        # dp[i] 表示從 days[i] 開始旅行的最小花費
        dp = [0] * (n + 1)
        # j 和 k 分別表示若當前購買 7 天票和 30 天票，則可以不用買票的「最大」日期下標
        j = k = n - 1
        for i in range(n - 1, -1, -1):
            d = days[i]
            while days[j] >= d + 7:
                j -= 1
            while days[k] >= d + 30:
                k -= 1
            # 轉移方程，j + 1 和 k + 1 是下次需要買票的日期
            dp[i] = min(costs[0] + dp[i + 1], costs[1] + dp[j + 1], costs[2] + dp[k + 1])
        return dp[0]
    
# class Solution(Solution1):
# class Solution(Solution2):
class Solution(Solution3):
    pass      
# @lc code=end

sol = Solution()
print(sol.mincostTickets([1,4,6,7,8,20], [2,7,15])) # 11
print(sol.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])) # 17

#
# @lcpr case=start
# [1,4,6,7,8,20]\n[2,7,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10,30,31]\n[2,7,15]\n
# @lcpr case=end

#

