# @algorithm @lc id=3191 lang=python3 
# @title maximum-score-after-applying-operations-on-a-tree


from en.Python3.mod.preImport import *
# @test([[0,1],[0,2],[0,3],[2,4],[4,5]],[5,2,5,2,1,1])=11
# @test([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]],[20,10,9,7,4,3,5])=40
class Solution:
    """
        Tree DP
    """
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = sum(values)

        def dfs(node, parent): # 要保留的節點分數
            if node != 0 and len(g[node]) == 1:
                return values[node]
            ans = values[node] # 保留這個節點的分數，則下面的節點都不用選
            d = 0 # 不保留這個節點的分數，則下面的節點都要選
            for x in g[node]:
                if x != parent:
                    d += dfs(x, node)
            return min(ans, d) # 選/不選，取最小值

        return ans - dfs(0, -1)