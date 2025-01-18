# @algorithm @lc id=435 lang=python3 
# @title non-overlapping-intervals


from en.Python3.mod.preImport import *
# @test([[1,2],[2,3],[3,4],[1,3]])=1
# @test([[1,2],[1,2],[1,2]])=2
# @test([[1,2],[2,3]])=0
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return self.solveByDP(intervals)
        return self.solveByGreedy(intervals)
    """
        1. Dynamic Programming
        Variation of Longest Increasing Subsequence (LIS)
    """
    def solveByDP(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0: return 0
        ans = 1 # 最大LIS長度
        intervals.sort(key=lambda x: x[0]) # 確保 start time 遞增
        # 因為si < ei, 所以確保 start time 遞增後，再考慮 ei 的 LIS 就可以了
        # dp[i] 表示 ei 的 LIS 長度
        dp = [1] * n
        for i in range(1, n):
            # for j in range(i): # 枚舉 i 前面的所有位置 j
            #     if intervals[j][1] <= intervals[i][0]: # si 可以接在 ej 後面
            #         dp[i] = max(dp[i], dp[j] + 1)
            for j in range(i-1, -1, -1): # 因為 intervals 已經排序過了，所以可以從後面往前找
                if intervals[j][1] <= intervals[i][0]: # si 可以接在 ej 後面
                    dp[i] = max(dp[i], dp[j] + 1)
                    break # Pruning, 不剪枝會 TLE
            ans = max(ans, dp[i])
        return (n - ans) # 最少需要刪除的區間數量
    """
        2. Greedy
        Early Deadline First (EDF)
    """
    def solveByGreedy(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1]) # 依照 end time 遞增排序
        right = intervals[0][1] #  最早的deadline
        ans = 1 # 最多可以保留的區間數量
        for st, et in intervals:
            if st >= right:
                ans += 1
                right = et
        return n - ans # 最少需要刪除的區間數量