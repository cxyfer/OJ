#
# @lc app=leetcode id=661 lang=python3
# @lcpr version=30204
#
# [661] Image Smoother
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                cnt = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n:
                            s += img[x][y]
                            cnt += 1
                ans[i][j] = s // cnt
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[100,200,100],[200,50,200],[100,200,100]]\n
# @lcpr case=end

#

