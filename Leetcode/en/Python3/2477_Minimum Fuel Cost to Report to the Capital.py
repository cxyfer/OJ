# @algorithm @lc id=2568 lang=python3 
# @title minimum-fuel-cost-to-report-to-the-capital


from en.Python3.mod.preImport import *
# @test([[0,1],[0,2],[0,3]],5)=3
# @test([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]],2)=7
# @test([],1)=0
class Solution:
    """
        想複雜了，以為是圖，結果是樹
        對於每個非0的節點，到0的路徑都是唯一的
        用DFS訪問每個節點，返回這個節點的子樹中所有節點的數量(包含自己)
        即到首都數浪會經過當前城市的人數(包含當前城市的代表)，計算到前一個城市的花費即可
    """
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1 # N = E + 1
        ans = 0

        g = [[] for _ in range(n)]
        for u, v in roads: # Undirected graph
            g[u].append(v)
            g[v].append(u)
        
        ans = 0
        def dfs(u: int, fa: int) -> int: # 返回這個節點的子樹中所有節點的數量(包含自己)。
            nonlocal ans
            s = 1 # 自己
            for v in g[u]: # 訪問子節點，即除了父節點以外的所有節點
                if v != fa: 
                    s += dfs(v, u)
            if u != 0: # 除了首都以外的節點
                ans += ceil(s / seats) * 1 # 前往上一個城市的車輛數，向上取整，代價固定為1
            return s
        dfs(0, -1)
        return ans

        