#
# @lc app=leetcode.cn id=2008 lang=python3
#
# [2008] 出租车的最大盈利
#
from preImport import *
# @lc code=start
class Solution:
    """
        DP + Binary Search
        本質上就是 Weighted Interval Scheduling 問題
        https://www.csie.ntu.edu.tw/~yvchen/f111-ada/
        dp[i]表示只接受前i個乘客的最大收益，對於第i個乘客，我們可以選擇接或不接
        若接的話則需要考慮上一個乘客是誰，
        - bisect.bisect_right回傳大於x的第一個下標(相當於C++中的upper_bound)，
        - bisect.bisect_left回傳大於等於x的第一個下標(相當於C++中的lower_bound)。
        目標是找到上一個相容(compatible)的乘客，也就是說上一個乘客的結束時間要小於等於當前乘客的開始時間。

    """
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        m = len(rides)
        rides.sort(key=lambda x: x[1]) # 按照結束時間由小到大排序，確保上一個相容(compatible)的區間若存在，其下標必在當前區間的下標之前
        dp = [0] * (m + 1) # m個區間
        for i, (st, ed, tip) in enumerate(rides):
            w = ed - st + tip # weight 
            # 找到「上一個」相容(compatible)的區間的下標
            j = bisect_right(rides, st, hi=i, key=lambda x: x[1]) - 1
            # left, right = 0, i
            # while left <= right: # [left, right]
            #     mid = (left + right) // 2
            #     if rides[mid][1] <= st:
            #         left = mid + 1
            #     else:
            #         right = mid - 1 
            # j = right
            dp[i+1] = max(dp[i], dp[j+1] + w)
        return dp[m]
# @lc code=end
sol = Solution()
print(sol.maxTaxiEarnings(5,[[2,5,4],[1,5,1]])) # 7
print(sol.maxTaxiEarnings(20,[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]])) # 20

