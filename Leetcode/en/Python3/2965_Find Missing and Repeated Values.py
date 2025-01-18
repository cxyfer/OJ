# @algorithm @lc id=3227 lang=python3 
# @title find-missing-and-repeated-values


from en.Python3.mod.preImport import *
# @test([[1,3],[2,2]])=[2,4]
# @test([[9,1,7],[8,9,2],[3,4,6]])=[9,5]
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        cnt = [0] * (n * n + 1)
        for i in range(n):
            for j in range(n):
                cnt[grid[i][j]] += 1
        ans1, ans2 = 0, 0
        for i in range(1, n * n + 1):
            if cnt[i] == 0:
                ans2 = i
            elif cnt[i] == 2:
                ans1 = i
        return [ans1, ans2]