#
# @lc app=leetcode id=3242 lang=python3
# @lcpr version=30204
#
# [3242] Design Neighbor Sum Service
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        n, m = len(grid), len(grid[0])
        ans1 = defaultdict(int)
        ans2 = defaultdict(int)
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < n and 0 <= ny < m:
                        ans1[val] += grid[nx][ny]
                for nx, ny in [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 1), (x - 1, y + 1)]:
                    if 0 <= nx < n and 0 <= ny < m:
                        ans2[val] += grid[nx][ny]
        self.ans1 = ans1
        self.ans2 = ans2

    def adjacentSum(self, value: int) -> int:
        return self.ans1[value]

    def diagonalSum(self, value: int) -> int:
        return self.ans2[value]

# @lc code=end



#
# @lcpr case=start
# ["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"][[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]\n
# @lcpr case=end

# @lcpr case=start
# ["NeighborSum", "adjacentSum", "diagonalSum"][[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]\n
# @lcpr case=end

#

