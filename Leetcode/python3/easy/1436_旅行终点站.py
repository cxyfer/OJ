#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#
from preImport import *
# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = defaultdict(int)
        for u, v in paths:
            outdegree[u] += 1
            outdegree[v] += 0 # 為了建立所有點的索引
        
        for node in outdegree:
            if outdegree[node] == 0:
                return node
        return ""
# @lc code=end
sol = Solution()
print(sol.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])) # "Sao Paulo"
print(sol.destCity([["B","C"],["D","B"],["C","A"]])) # "A"
print(sol.destCity([["A","Z"]])) # "Z"
