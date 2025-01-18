#
# @lc app=leetcode.cn id=2374 lang=python3
#
# [2374] 边积分最高的节点
#

# @lc code=start
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        for i, to in enumerate(edges):
            scores[to] += i
        ans = 0
        for i, s in enumerate(scores):
            if s > scores[ans]:
                ans = i
        return ans
            
# @lc code=end

