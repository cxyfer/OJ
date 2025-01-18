#
# @lc app=leetcode id=1791 lang=python3
# @lcpr version=30204
#
# [1791] Find Center of Star Graph
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        deg = [0] * (n + 1)
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
        return deg.index(n - 1)
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,3],[4,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[5,1],[1,3],[1,4]]\n
# @lcpr case=end

#

