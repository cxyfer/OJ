#
# @lc app=leetcode id=3414 lang=python3
# @lcpr version=30204
#
# [3414] Maximum Score of Non-overlapping Intervals
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
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[1])
        # dp[i][j] 表示在前 i 個區間中，選擇至多 j 個區間所能獲得的最大分數
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        for i, (l, r, w, idx) in enumerate(arr):
            j = bisect_left(arr, l, hi=i, key=lambda x: x[1]) - 1
            for k in range(1, 5):
                s2, res2 = dp[j+1][k-1]
                new_s, new_res = s2 + w, sorted(res2 + [idx])
                
                if new_s > dp[i][k][0]:
                    dp[i+1][k] = (new_s, new_res)
                elif new_s == dp[i][k][0]:
                    dp[i+1][k] = (new_s, min(dp[i][k][1], new_res))
                else:
                    dp[i+1][k] = dp[i][k]
        return dp[n][4][1]
# @lc code=end

sol = Solution()
sol.maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]])
print(sol.maximumWeight([[1,1,1000000000],[1,1,1000000000],[1,1,1000000000],[1,1,1000000000]])) # [0]
#
# @lcpr case=start
# [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]\n
# @lcpr case=end

#

