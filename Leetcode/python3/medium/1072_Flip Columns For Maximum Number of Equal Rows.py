#
# @lc app=leetcode id=1072 lang=python3
# @lcpr version=30204
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mask = (1 << len(matrix[0])) - 1
        cnt = defaultdict(int)
        for row in matrix:
            x = 0
            for i, val in enumerate(row):
                if val == 1:
                    x |= 1 << i
            cnt[x if row[0] == 0 else x ^ mask] += 1
        return max(cnt.values())
# @lc code=end



#
# @lcpr case=start
# [[0,1],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[0,0,1],[1,1,0]]\n
# @lcpr case=end

#

