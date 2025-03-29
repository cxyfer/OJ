#
# @lc app=leetcode id=54 lang=python3
# @lcpr version=30201
#
# [54] Spiral Matrix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        ans = [-1] * (m * n)
        vis = [[False for _ in range(n)] for _ in range(m)]
        x, y = 0, 0
        cd = 0 # current direction
        for i in range(m * n):
            ans[i] = matrix[x][y]
            vis[x][y] = True
            nx, ny = x + dirs[cd][0], y + dirs[cd][1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or vis[nx][ny]: # change direction
                cd = (cd + 1) % 4
                nx, ny = x + dirs[cd][0], y + dirs[cd][1]
            x, y = nx, ny
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

