#
# @lc app=leetcode id=2713 lang=python3
# @lcpr version=30203
#
# [2713] Maximum Strictly Increasing Cells in a Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i, j))
        row_max, col_max = [0] * m, [0] * n
        for x, pos in sorted(g.items(), key = lambda x: x[0]):
            # 要先把轉移的結果算出來，否則會被覆蓋
            res = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            for (i, j), r in zip(pos, res):
                row_max[i] = max(row_max[i], r)
                col_max[j] = max(col_max[j], r)
        return max(row_max) # or return max(col_max)
# @lc code=end

[[1,-8],[4,4],[-3,-9]]
sol = Solution()
print(sol.maxIncreasingCells([[1,-8],[4,4],[-3,-9]])) # 4


#
# @lcpr case=start
# [[3,1],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,1,6],[-9,5,7]]\n
# @lcpr case=end

#

