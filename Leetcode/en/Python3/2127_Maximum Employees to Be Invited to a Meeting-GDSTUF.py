# @algorithm @lc id=2246 lang=python3 
# @title maximum-employees-to-be-invited-to-a-meeting


from en.Python3.mod.preImport import *
# @test([2,2,1,2])=3
# @test([1,2,0])=3
# @test([3,0,1,4,1])=4
class Solution:
    """
        内向基环树 (pseudotree)，由基环树组成的森林叫基环树森林 (pseudoforest)
    """
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n # in-degree
        for f in favorite:
            indeg[f] += 1

        rg = [[] for _ in range(n)] # reverse graph
        q = deque(i for i, deg in enumerate(indeg) if deg == 0)
        while q: # topological sort, BFS，剪枝
            x = q.popleft()
            y = favorite[x] # 根據題意，x 的最愛是 y，所以只有一條out-edge
            rg[y].append(x) # 反向建圖
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)

        # 通過 reverse graph，找到最深的路徑
        def rdfs(x: int) -> int:
            max_depth = 1
            for son in rg[x]:
                max_depth = max(max_depth, rdfs(son) + 1)
            return max_depth

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(indeg):
            if d == 0: # 非基環上的點，則跳過，或者已經訪問過，則跳過
                continue

            # 遍歷基環上的點
            indeg[i] = 0 # 將基環上的點的入度標記為 0，避免重複訪問
            ring_size = 1 # 基環長度
            x = favorite[i] 
            while x != i:
                indeg[x] = 0 # 將基環上的點的in-degree標記為 0，避免重複訪問
                ring_size += 1
                x = favorite[x]

            if ring_size == 2: # 基環長度為 2，則兩條最長路徑的長度之和即為答案
                sum_chain_size += rdfs(i) + rdfs(favorite[i]) # 累加兩條最長路徑的長度
            else:
                max_ring_size = max(max_ring_size, ring_size) # 取所有基環長度的最大值
        return max(max_ring_size, sum_chain_size)