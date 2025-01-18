#
# @lc app=leetcode id=1235 lang=python3
# @lcpr version=30204
#
# [1235] Maximum Profit in Job Scheduling
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
Dynamic Programming + Binary Search
Weighted Job Scheduling / Weighted Interval Scheduling
Similar:
    - 2008. Maximum Earnings From Taxi 1872
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # 按照結束時間由小到大排序，確保上一個相容(compatible)的區間若存在，其下標必在當前區間的下標之前
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        # dp[i] 表示前 i 個工作所能獲得的最大利潤
        dp = [0] * (n + 1) # n個區間
        for i, (st, _, w) in enumerate(jobs):
            # 找到上一個相容(compatible)的區間的下標
            j = bisect_right(jobs, st, hi=i, key=lambda x: x[1]) - 1
            dp[i+1] = max(dp[i], dp[j+1] + w)
        return dp[n]
# @lc code=end

sol = Solution()
print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])) # 120

#
# @lcpr case=start
# [1,2,3,3]\n[3,4,5,6]\n[50,10,40,70]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,6]\n[3,5,10,6,9]\n[20,20,100,70,60]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n[2,3,4]\n[5,6,4]\n
# @lcpr case=end

#

