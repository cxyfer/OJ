#
# @lc app=leetcode id=3127 lang=python3
# @lcpr version=30204
#
# [3127] Make a Square with the Same Color
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m - 1):
            for j in range(n - 1):
                cnt = [0, 0]
                for x in range(2):
                    for y in range(2):
                        cnt[0 if grid[i+x][j+y] == 'B' else 1] += 1
                if cnt[0] >= 3 or cnt[1] >= 3:
                    return True
        return False
# @lc code=end



#
# @lcpr case=start
# [["B","W","B"],["B","W","W"],["B","W","B"]]\n
# @lcpr case=end

# @lcpr case=start
# [["B","W","B"],["W","B","W"],["B","W","B"]]\n
# @lcpr case=end

# @lcpr case=start
# [["B","W","B"],["B","W","W"],["B","W","W"]]\n
# @lcpr case=end

#

