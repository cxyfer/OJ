# @algorithm @lc id=1547 lang=python3 
# @title destination-city


from en.Python3.mod.preImport import *
# @test([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])="Sao Paulo"
# @test([["B","C"],["D","B"],["C","A"]])="A"
# @test([["A","Z"]])="Z"
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
        