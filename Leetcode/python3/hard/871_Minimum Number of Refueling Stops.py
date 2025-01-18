#
# @lc app=leetcode id=871 lang=python3
# @lcpr version=30204
#
# [871] Minimum Number of Refueling Stops
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. 記憶化搜索
    2. 刷表法
    3. 貪心 + 堆
"""
class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)

        # 定義 dfs(i, j) 表示考慮 [0, i] 範圍中的加油站，加了 j 次油能到達的最遠距離
        @cache
        def dfs(i, j):
            if j == 0:
                return startFuel
            if i + 1 < j: # 如果加油次數 j 超過加油站數量 i + 1，則無法到達
                return 0
            pos, fuel = stations[i]
            # 若當前站點 i 不加油，可以求解子問題：[0, i - 1] 範圍中的加油站，加了 j 次油能到達的最遠距離
            res = dfs(i - 1, j) # 不加油
            # 若當前站點 i 加油，可以求解子問題：[0, i - 1] 範圍中的加油站，加了 j - 1 次油能到達的最遠距離
            # 但需要先判定是否能到達當前站點 i
            if dfs(i - 1, j - 1) >= pos:
                res = max(res, dfs(i - 1, j - 1) + fuel) # 加油
            return res
        
        for k in range(n + 1):
            if dfs(n - 1, k) >= target:
                return k
        return -1
    
class Solution2:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 雖然題目敘述沒有寫，但加油站的順序是按位置排序的，故可以不用排序
        # stations.sort(key=lambda x: x[0]) 
        n = len(stations)
        # dp[k] 表示加了 k 次油能走的最遠距離
        dp = [startFuel] + [0] * n
        for i, (pos, fuel) in enumerate(stations): # 枚舉每一個加油站
            for j in range(i, -1, -1): # 枚舉到達第 i 個加油站時的加油次數
                if dp[j] >= pos: # 如果加油次數 j 能到達加油站 pos
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel) # 更新加油次數 j + 1 能到達的最遠距離
        # 枚舉加油次數，找到能到達終點的最小加油次數
        for i, pos in enumerate(dp):
            if pos >= target:
                return i
        return -1
    
class Solution3:
    """
        Greedy + Heap
        先走道當前油量能到的最遠距離，若不足以到達終點，則選擇油量最多的加油站加油
        用 Heap 維護能到達的加油站的油量
    """
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans = 0
        cur = startFuel # 當前能到達的距離
        hp = []
        stations.append([target, 0])
        for pos, fuel in stations:
            if cur >= target:
                break
            while pos > cur:
                if not hp:
                    return -1
                cur += -heappop(hp)
                ans += 1
            heappush(hp, -fuel)
        return ans

class Solution(Solution1):
# class Solution(Solution2):  
# class Solution(Solution3):
    pass
# @lc code=end

sol = Solution()
print(sol.minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]])) # 2

#
# @lcpr case=start
# 1\n1\n[]\n
# @lcpr case=end

# @lcpr case=start
# 100\n1\n[[10,100]]\n
# @lcpr case=end

# @lcpr case=start
# 100\n10\n[[10,60],[20,30],[30,30],[60,40]]\n
# @lcpr case=end

#

