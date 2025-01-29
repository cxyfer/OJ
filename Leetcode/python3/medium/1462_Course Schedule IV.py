#
# @lc app=leetcode id=1462 lang=python3
# @lcpr version=30204
#
# [1462] Course Schedule IV
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def checkIfPrerequisite(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [[False] * n for _ in range(n)]
        
        ind = [0] * n
        g = [[] for _ in range(n)]
        for u, v in edges:
            ind[v] += 1
            g[u].append(v)
        
        q = deque([i for i, d in enumerate(ind) if d == 0])
        while q:
            u = q.popleft()
            for v in g[u]:
                ans[u][v] = True
                # 1. 枚舉前面的點
                # for i in range(n):
                #     ans[i][v] |= ans[i][u]
                ind[v] -= 1
                if ind[v] == 0:
                    q.append(v)

        # 2. 直接跑 Floyd-Warshall
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    ans[u][v] |= ans[u][k] and ans[k][v]

        return [ans[u][v] for u, v in queries]
# @lc code=end

sol = Solution()
# [false, true]
print(sol.checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))
# [true,false,true,false]0
print(sol.checkIfPrerequisite(5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]]))

#
# @lcpr case=start
# 2\n[[1,0]]\n[[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[]\n[[1,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,2],[1,0],[2,0]]\n[[1,0],[1,2]]\n
# @lcpr case=end

#

