#
# @lc app=leetcode id=2924 lang=python3
# @lcpr version=30204
#
# [2924] Find Champion II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ind = [0] * n
        for u, v in edges:
            ind[v] += 1
        ans = -1
        for u in range(n):
            if ind[u]: continue
            if ans != -1:
                return -1
            ans = u
        return ans
# @lc code=end



#
# @lcpr case=start
# 3\n[[0,1],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,2],[1,3],[1,2]]\n
# @lcpr case=end

#

