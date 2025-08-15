#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Dynamic Programming (LIS)
2. Greedy
"""
# @lc code=start
class Solution1:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        ans = n  # 所求為 n - LIS 長度
        intervals.sort(key = lambda p : p[0])  # 確保 start time 遞增
        print(intervals)
        # 因為 si < ei, 所以確保 start time 遞增後，再考慮 end time 的 LIS 就可以了
        # f[i] 表示以 intervals[i] 為結尾的 LIS 長度
        f = [1] * n
        for i, (st, ed) in enumerate(intervals):
            for j in range(i - 1, -1, -1):
                if intervals[j][1] <= st:  # 當前 intervals[i] 可以接在 intervals[j] 後面
                    f[i] = max(f[i], f[j] + 1)
                    # 因為 si 遞增，所以若 f[j - 1] 可以接在 f[k] 後，那麼 f[j] 也可以接在 f[k] 後，所以 f[j] 一定不差於 f[j - 1]
                    break  # Pruning, 不剪枝會 TLE
            ans = min(ans, n - f[i])
        return ans

class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda p : p[1])
        ans = n
        r = float("-inf")
        for st, ed in intervals:
            if st >= r:
                ans -= 1
                r = ed
        return ans
    
# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()