#
# @lc app=leetcode id=2127 lang=python3
# @lcpr version=30204
#
# [2127] Maximum Employees to Be Invited to a Meeting
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
內向基環樹 (pseudotree)，由基環樹组成的森林叫基環樹森林 (pseudoforest)
"""
# @lc code=start
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n
        for f in favorite:
            indeg[f] += 1
        
        rg = [[] for _ in range(n)]
        q = deque(i for i, d in enumerate(indeg) if d == 0)
        while q: # 拓樸排序
            u = q.popleft()
            v = favorite[u]
            rg[v].append(u) # 反向建圖
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        # 通過 reverse graph，找到最大樹高
        def rdfs(u: int) -> int:
            res = 1
            for v in rg[u]:
                res = max(res, rdfs(v) + 1)
            return res
        
        max_ring_size = sum_chain_size = 0
        for u, d in enumerate(indeg): # 遍歷所有基環上的點
            if d == 0: # 入度為0代表非基環上的點或者已經訪問過，跳過
                continue

            # 找到基環上的所有點
            rings = [u]
            v = favorite[u]
            while v != u:
                rings.append(v)
                v = favorite[v]
            for v in rings:
                indeg[v] = 0 # 將基環上的點的入度標記為 0，避免重複訪問
            
            # 若基環長度為 2，則可以選擇基環以及兩側的最長鏈，且其仍然可以展開為鏈，因此可以有多個長度為 2 的基環
            if len(rings) == 2: 
                sum_chain_size += rdfs(u) + rdfs(favorite[u])
            # 若基環長度大於 2，則只能選擇基環本身
            else:
                max_ring_size = max(max_ring_size, len(rings))
        return max(max_ring_size, sum_chain_size)
# @lc code=end

sol = Solution()
print(sol.maximumInvitations([2,2,1,2]))  # 3
print(sol.maximumInvitations([1,2,0]))  # 3
print(sol.maximumInvitations([3,0,1,4,1]))  # 4

#
# @lcpr case=start
# [2,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,0,1,4,1]\n
# @lcpr case=end

#

