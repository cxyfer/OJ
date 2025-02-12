#
# @lc app=leetcode id=3446 lang=python3
# @lcpr version=30204
#
# [3446] Sort Matrix by Diagonals
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(list)
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                mp[i - j].append(val)
        for k, arr in mp.items():
            arr.sort(reverse=(False if k < 0 else True))
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                row[j] = mp[i - j].pop(0)
        return grid
# @lc code=end

sol = Solution()
print(sol.sortMatrix([[1,7,3],[9,8,2],[4,5,6]]))

#
# @lcpr case=start
# [[1,7,3],[9,8,2],[4,5,6]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#

