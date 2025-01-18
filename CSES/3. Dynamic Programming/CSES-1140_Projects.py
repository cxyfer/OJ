"""
    Weighted Interval Scheduling
"""
from bisect import *
n = int(input())
projects = [tuple(map(int, input().split())) for _ in range(n)]
projects.sort(key=lambda x: x[1]) # 按照結束時間由小到大排序，確保上一個相容(compatible)的區間若存在，其下標必在當前區間的下標之前

dp = [0] * (n + 1)
for i, (st, ed, w) in enumerate(projects):
    j = bisect_right(projects, st, hi=i, key=lambda x: x[1]) - 1 # 找到「上一個」相容(compatible)的區間的下標
    dp[i+1] = max(dp[i], dp[j+1] + w)
print(dp[n])

# class Solution:
#     def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
#         m = len(rides)
#         rides.sort(key=lambda x: x[1]) # 按照結束時間由小到大排序，確保上一個相容(compatible)的區間若存在，其下標必在當前區間的下標之前
#         dp = [0] * (m + 1) # m個區間
#         for i, (st, ed, tip) in enumerate(rides):
#             w = ed - st + tip # weight 
#             j = bisect_right(rides, st, hi=i, key=lambda x: x[1]) - 1 # 找到「上一個」相容(compatible)的區間的下標
#             dp[i+1] = max(dp[i], dp[j+1] + w)
#         return dp[m]