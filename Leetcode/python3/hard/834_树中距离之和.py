#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#
from preImport import *
# @lc code=start
class Solution:
    """
        為何可以從 Floyd-Warshall O(n^3) 退化到 換根 DP O(n)
        https://leetcode.cn/problems/sum-of-distances-in-tree/solutions/437205/shu-zhong-ju-chi-zhi-he-by-leetcode-solution/comments/2066484
    """
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = [0] * n
        size = [1] * n
        def dfs(u: int, fa: int, depth: int) -> None:
            ans[0] += depth
            for v in g[u]:
                if v != fa:
                    dfs(v, u, depth + 1)
                    size[u] += size[v]

        dfs(0, -1, 0) # 先以 0 為根，計算0到其他點的距離和、以及每個子樹的大小

        def reroot(u: int, fa: int) -> None:
            for v in g[u]:
                if v != fa:
                    ans[v] = ans[u] + (n - size[v]) - size[v]
                    reroot(v, u)
        reroot(0, -1) # 換根
        return ans
# @lc code=end

