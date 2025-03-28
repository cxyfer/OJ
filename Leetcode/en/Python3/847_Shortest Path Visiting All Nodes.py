# @algorithm @lc id=877 lang=python3 
# @title shortest-path-visiting-all-nodes


from en.Python3.mod.preImport import *
# @test([[1,2,3],[0],[0],[0]])=4
# @test([[1],[0,2,4],[1,3,4],[2],[1,2]])=4
class Solution:
    """
        BFS + bitmask
    """
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((i, 1 << i, 0) for i in range(n)) # u, mask, dist
        # visited 保存已經走過的節點以及走訪到該節點時的 mask 狀態
        visited = { (i, 1 << i) for i in range(n) }
        ans = 0
        
        while q:
            u, mask, dist = q.popleft()
            if mask == (1 << n) - 1:
                ans = dist
                break
            for v in graph[u]: # 搜尋相鄰的節點
                # mask 用來回溯用，另設一個 mask_v 來記錄走過的節點
                mask_v = mask | (1 << v) # 將 mask_v 的第 v 位設為 1
                if (v, mask_v) not in visited:
                    q.append((v, mask_v, dist + 1))
                    visited.add((v, mask_v))
        return ans