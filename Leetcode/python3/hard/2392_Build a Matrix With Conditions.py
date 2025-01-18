#
# @lc app=leetcode id=2392 lang=python3
# @lcpr version=30204
#
# [2392] Build a Matrix With Conditions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Topological sort
"""
from graphlib import TopologicalSorter

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort1(conditions: List[List[int]]) -> List[int]:
            ts = TopologicalSorter()
            for x in range(k):
                ts.add(x)
            for x, y in conditions: # x 必須在 y 之前
                ts.add(y-1, x-1) # (node, *predecessors)
            pos = [0] * k
            try:
                for i, x in enumerate(ts.static_order()): 
                    pos[x] = i
            except ValueError:
                return []
            return pos
        def topological_sort2(conditions: List[List[int]]) -> List[int]:
            g = [[] for _ in range(k)] # adjacency list
            deg = [0] * k # in-degree
            for x, y in conditions: # x 必須在 y 之前
                g[x - 1].append(y - 1)
                deg[y - 1] += 1
            order = [] # 拓樸排序的結果，第 i 個元素是 x
            q = deque(i for i, d in enumerate(deg) if d == 0)
            while q:
                x = q.popleft()
                order.append(x)
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 0:
                        q.append(y)
            pos = [0] * k # 把「第 i 個元素是 x」轉換為「x 在第 i 個位置」
            for i, x in enumerate(order):
                pos[x] = i
            return pos if len(order) == k else []
        topo_sort = topological_sort2
        row, col = topo_sort(rowConditions), topo_sort(colConditions)
        if not row or not col:
            return []
        ans = [[0] * k for _ in range(k)]
        for x, (i, j) in enumerate(zip(row, col)): # x 在第 i 橫列，第 j 直行
            ans[i][j] = x + 1
        return ans
# @lc code=end

sol = Solution()
print(sol.buildMatrix(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]])) 
print(sol.buildMatrix(3, [[1, 2], [2, 3], [3, 1], [2, 3]], [[2, 1]]))

#
# @lcpr case=start
# 3\n[[1,2],[3,2]]\n[[2,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,2],[2,3],[3,1],[2,3]]\n[[2,1]]\n
# @lcpr case=end

#

