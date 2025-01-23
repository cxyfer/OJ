#
# @lc app=leetcode id=2944 lang=python3
# @lcpr version=30204
#
# [2944] Minimum Number of Coins for Fruits
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Memoization
    令 f(i) 表示從第 i 個水果開始買，買到最後一個水果的最小花費
    枚舉下一次要買的水果
    - 第 i + 1 個到第 2 * i 個可買可不買
    - 但若中間都沒買，則一定要買第 2 * i + 1 個
    故枚舉 i + 1 到 2 * i + 1 的水果即可
2. Tabulation
3. DP + Monotonic Queue
"""
# @lc code=start
class Solution1:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def f(i: int) -> int: # 從第 i 個水果開始買，買到最後一個水果的最小花費
            if i * 2 >= n: # 剪枝：已經可以買到剩下所有的水果
                return prices[i - 1]
            res = f(i * 2 + 1) # 中間都沒買，一定要買第 2 * i + 1 個
            for j in range(i + 1, i + i + 1): # 枚舉中間可買可不買的水果
                res = min(res, f(j))
            return prices[i - 1] + res
        return f(1)
    
class Solution2:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        f = [0] * (n + 1)
        for i in range(n, 0, -1):
            if i * 2 >= n:
                f[i] = prices[i - 1] + 0
            else:
                f[i] = prices[i - 1] + min(f[i + 1:i * 2 + 2])
        return f[1]
    
class Solution3:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        q = deque() # (i, f[i]), f(i) 是單調遞減的
        # q = deque([(n + 1, 0)]) # 也可以插一個哨兵，這樣就不用考慮 i * 2 >= n 的情況
        for i in range(n, 0, -1):
            # 1. 彈出右側超過窗口範圍的元素
            while q and q[-1][0] > i * 2 + 1: 
                q.pop()
            # 2. 計算 f[i]
            f = prices[i - 1] + (0 if i * 2 >= n else q[-1][1])
            # 3. 將 (i, f[i]) 加入窗口左側
            while q and f <= q[0][1]: # 彈出左側大於等於 f[i] 的元素
                q.popleft()
            q.appendleft((i, f))
        return q[0][1]

# class Solution(Solution1):
# class Solution(Solution2):
class Solution(Solution3):
    pass
# @lc code=end

sol = Solution()
print(sol.minimumCoins([3,1,2])) # 4
# print(sol.minimumCoins([1,10,1,1])) # 2
# print(sol.minimumCoins([1,37,19,38,11,42,18,33,6,37,15,48,23,12,41,18,27,32])) # 37
#
# @lcpr case=start
# [3,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,10,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [26,18,6,12,49,7,45,45]\n
# @lcpr case=end

#

