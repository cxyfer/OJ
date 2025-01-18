# @algorithm @lc id=1352 lang=python3 
# @title maximum-profit-in-job-scheduling


from en.Python3.mod.preImport import *
# @test([1,2,3,3],[3,4,5,6],[50,10,40,70])=120
# @test([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60])=150
# @test([1,1,1],[2,3,4],[5,6,4])=6
class Solution:
    """
        Dynamic Programming
        Weighted Job Scheduling / Weighted Interval Scheduling
        Similar:
            - 2023-12-08 2008. Maximum Earnings From Taxi 1872
    """
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        # 按照結束時間由小到大排序，確保上一個相容(compatible)的區間若存在，其下標必在當前區間的下標之前
        jobs = sorted(zip(endTime, startTime, profit)) 
        dp = [0] * (n + 1) # n個區間
        for i, (ed, st, w) in enumerate(jobs):
            # 找到「上一個」相容(compatible)的區間的下標
            # j = bisect_right(jobs, st, hi=i, key=lambda x: x[0]) - 1 
            j = bisect_right(jobs, (st, float("inf")), hi=i) - 1 
            dp[i+1] = max(dp[i], dp[j+1] + w)
        return dp[n]