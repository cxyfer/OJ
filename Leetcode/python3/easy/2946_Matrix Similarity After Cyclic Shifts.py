#
# @lc app=leetcode id=2946 lang=python3
#
# [2946] Matrix Similarity After Cyclic Shifts
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        return k == 0 or all(row[-k:] + row[:-k] == row for row in mat)

class Solution2:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return all(val == row[(i + k) % len(row)] for row in mat for i, val in enumerate(row))

Solution = Solution1
# Solution = Solution2
# @lc code=end

