#
# @lc app=leetcode id=2742 lang=python3
# @lcpr version=30204
#
# [2742] Painting the Walls
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Dynamic Programming
    1. Dynamic Programming
        令 dp[i][j][k] 為考慮前 i 堵牆，付費時間為 j，免費時間為 k 的最小花費 
        -> MLE -> 降維
        令 dp[i][j] 為考慮前 i 堵牆，付費時間減去免費時間為 j 的最小花費 
    2. Variance of 0-1 knapsack problem
        付費時間 >= 免費刷牆數 = n - 付費刷牆數
        -> 付費時間 + 付費刷牆數 >= n
        將每堵牆視為體積為 time[i] + 1 的物品，即可轉換為
        0-1 背包問題，至少裝體積總和為 n 的物品
"""


class Solution1x:  # MLE

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if j - k >= i:
                return 0
            if i == 0:
                return 0 if j >= k else float('inf')
            # 免費刷第 i 堵牆 / 付費刷第 i 堵牆 (下標為 i-1)
            return min(dfs(i - 1, j, k + 1),
                       cost[i - 1] + dfs(i - 1, j + time[i - 1], k))

        return dfs(n, 0, 0)


class Solution1:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def dfs(i: int, j: int) -> int:
            if j >= i:  # 剩餘的付費時間超過牆數
                return 0
            if i == 0:
                # return 0 if j >= 0 else float('inf') 
                return float('inf') # 已經檢查過 j >= i 的情況
            return min(dfs(i - 1, j - 1), # 免費刷第 i 堵牆 (下標為 i-1 )
                       dfs(i - 1, j + time[i - 1]) + cost[i - 1]) # 付費刷第 i 堵牆

        return dfs(n, 0)

class Solution2a:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache  # Memoization
        def dfs(i: int, j: int) -> int:  # i: 已經考慮到第 i 堵牆，j: 還需要的體積
            if j <= 0:
                return 0
            if i == 0:
                return float('inf')
            return min(dfs(i - 1, j), # 不選
                       dfs(i - 1, j - (time[i - 1] + 1)) + cost[i - 1]) # 選
        
        return dfs(n, n)


class Solution2b:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n]


# class Solution(Solution1):
class Solution(Solution2a):
# class Solution(Solution2b):
    pass


# @lc code=end

sol = Solution()
print(sol.paintWalls([1, 2, 3, 2], [1, 2, 3, 2]))  # 3
print(sol.paintWalls([2, 3, 4, 2], [1, 1, 1, 1]))  # 4

#
# @lcpr case=start
# [1,2,3,2]\n[1,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,2]\n[1,1,1,1]\n
# @lcpr case=end

#
