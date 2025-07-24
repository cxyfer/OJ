#
# @lc app=leetcode id=2322 lang=python3
#
# [2322] Minimum Score After Removals on a Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 樹上 DFS 求出子樹異或和，並求出 DFS 序
        f = [0] * n
        dfni, dfno = [0] * n, [0] * n
        t = 0
        def dfs(u, fa):
            nonlocal t
            t += 1
            dfni[u] = t
            f[u] = nums[u]
            for v in g[u]:
                if v != fa:
                    dfs(v, u)
                    f[u] ^= f[v]
            dfno[u] = t
        dfs(0, -1)

        # 判斷 v 是否在 u 的子樹中
        def query(u: int, v: int) -> bool:
            # assert u != v
            return dfni[u] < dfni[v] <= dfno[u]
        # 計算三個數的最大值和最小值的差
        def calc(x: int, y: int, z: int) -> int:
            return max(x, y, z) - min(x, y, z)
        
        # 枚舉切斷的兩條邊，求出兩個子樹的異或和，並求出兩個子樹的異或和的異或和
        ans = float('inf')
        for i, (u1, v1) in enumerate(edges):
            u1, v1 = (u1, v1) if query(u1, v1) else (v1, u1)
            for j in range(i + 1, n - 1):
                u2, v2 = edges[j]
                u2, v2 = (u2, v2) if query(u2, v2) else (v2, u2)
                if query(v1, v2):  # v2 在 v1 的子樹中
                    ans = min(ans, calc(f[v2], f[v1] ^ f[v2], f[0] ^ f[v1]))
                elif query(v2, v1):  # v1 在 v2 的子樹中
                    ans = min(ans, calc(f[v1], f[v2] ^ f[v1], f[0] ^ f[v2]))
                else:  # 兩個子樹不相交
                    ans = min(ans, calc(f[v1], f[v2], f[0] ^ f[v1] ^ f[v2]))
                if ans == 0:
                    return 0
        return ans
# @lc code=end

