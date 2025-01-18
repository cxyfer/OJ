#
# @lc app=leetcode id=840 lang=python3
# @lcpr version=30204
#
# [840] Magic Squares In Grid
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def isMagic(a, b, c, d, e, f, g, h, i):
            cnt = Counter([a, b, c, d, e, f, g, h, i])
            return all(cnt[k] == 1 for k in range(1, 10)) \
                   and (a + b + c == d + e + f == g + h + i \
                    == a + d + g == b + e + h == c + f + i \
                    == a + e + i == c + e + g == 15)
        
        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if grid[i+1][j+1] != 5:
                    continue
                if isMagic(grid[i][j], grid[i][j + 1], grid[i][j + 2], 
                           grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                           grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]):
                    ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [[4,3,8,4],[9,5,1,9],[2,7,6,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[8]]\n
# @lcpr case=end

#

