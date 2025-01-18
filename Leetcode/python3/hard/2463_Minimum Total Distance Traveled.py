#
# @lc app=leetcode id=2463 lang=python3
# @lcpr version=30204
#
# [2463] Minimum Total Distance Traveled
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    為使移動距離最小，每個 factory 應該修一段連續位置上的機器人，
    可以用反證法證明，若某個 factory 修了不相連的機器人，
    則可以把其中一個機器人換到其他 factory 修，其他機器人位置不變，
    這樣一定能使新的總距離小於等於原來的總距離。
"""
class Solution1:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()

        # 令 dfs(i, j) 為前 i+1 個工廠修了 j+1 個機器人所需要的最小距離
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0: # 沒有 factory 了
                return 0 if j < 0 else float('inf') # 如果還有機器人，則不合法
            if j < 0: # 剪枝，沒有機器人了
                return 0
            res = dfs(i - 1, j) # factory[i] 修 0 個機器人
            dist = 0
            pos, limit = factory[i]
            for k in range(limit): # 枚舉 factory[i] 修 k + 1 個機器人
                if j - k < 0:
                    break
                dist += abs(robot[j - k] - pos)
                res = min(res, dist + dfs(i - 1, j - (k + 1)))
            return res
        return dfs(m - 1, n - 1)
    
class Solution2:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()

        # 令 f[i][j] 為前 i 個工廠修了 j 個機器人所需要的最小距離
        f = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 0
        for i, (pos, limit) in enumerate(factory, 1):
            for j in range(n + 1):
                f[i][j] = f[i - 1][j] # factory[i] 修 0 個機器人
                dist = 0
                for k in range(1, limit + 1):
                    if j - k < 0:
                        break
                    dist += abs(robot[j - k] - pos)
                    f[i][j] = min(f[i][j], dist + f[i - 1][j - k])
        return f[m][n]

class Solution3:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()

        # 令 f[i][j] 為前 i 個工廠修了 j 個機器人所需要的最小距離
        f = [0] + [float('inf')] * n
        for pos, limit in factory:
            new_f = f.copy()
            for j in range(n + 1):
                new_f[j] = f[j] # factory[i] 修 0 個機器人
                dist = 0
                for k in range(1, limit + 1):
                    if j - k < 0:
                        break
                    dist += abs(robot[j - k] - pos)
                    new_f[j] = min(new_f[j], dist + f[j - k])
            f = new_f
        return f[n]
    
class Solution4:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()

        # 令 f[i][j] 為前 i 個工廠修了 j 個機器人所需要的最小距離
        f = [0] + [float('inf')] * n    
        for pos, limit in factory:
            for j in range(n, -1, -1):
                dist = 0
                for k in range(1, limit + 1):
                    if j - k < 0:
                        break
                    dist += abs(robot[j - k] - pos)
                    f[j] = min(f[j], dist + f[j - k])
        return f[n]
    
# class Solution(Solution1):
# class Solution(Solution2):
# class Solution(Solution3):
class Solution(Solution4):
    pass
# @lc code=end

sol = Solution()
print(sol.minimumTotalDistance([0,4,6], [[2,2],[6,2]])) # 4
print(sol.minimumTotalDistance([1,-1], [[-2,1],[2,1]])) # 2
print(sol.minimumTotalDistance([9,11,99,101], [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]])) # 6

#
# @lcpr case=start
# [0,4,6]\n[[2,2],[6,2]]\n
# @lcpr case=end

# @lcpr case=start
# [1,-1]\n[[-2,1],[2,1]]\n
# @lcpr case=end

#

