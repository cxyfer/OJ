from typing import List

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

sol = Solution()
print(sol.findMissingAndRepeatedValues([[1,3],[2,2]])) # [2,4]
print(sol.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])) # [9,5]