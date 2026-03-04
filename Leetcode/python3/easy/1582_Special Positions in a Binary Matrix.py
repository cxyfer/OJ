#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row = [0] * m
        col = [0] * n
        for i, line in enumerate(mat):
            for j, x in enumerate(line):
                row[i] += x
                col[j] += x
        
        ans = 0
        for i, line in enumerate(mat):
            for j, x in enumerate(line):
                if x == 1 and row[i] == 1 and col[j] == 1:
                    ans += 1
        return ans

class Solution2:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols = []
        for c in zip(*mat):
            cols.append(sum(c))
        ans = 0
        for row in mat:
            if sum(row) != 1:
                continue
            j = row.index(1)
            ans += (cols[j] == 1)
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

