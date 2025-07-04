#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        memo = [[[float('-inf')] * k for _ in range(2)] for _ in range(n)]
        # @cache
        def f(u: int, fa: int, p: int, d: int) -> int:
            if memo[u][p][d] != float('-inf'):
                return memo[u][p][d]
            res1 = nums[u] * (-1 if p & 1 else 1)
            for v in g[u]:
                if v == fa:
                    continue
                res1 += f(v, u, p, min(d + 1, k - 1))
            if d == k - 1:
                res2 = nums[u] * (1 if p & 1 else -1)
                for v in g[u]:
                    if v == fa:
                        continue
                    res2 += f(v, u, p ^ 1, 0)
                memo[u][p][d] = max(res1, res2)
            else:
                memo[u][p][d] = res1
            return memo[u][p][d]
        return f(0, -1, 0, k - 1)

class Solution2:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(edges) + 1
        g0 = [[] for _ in range(n)]
        for u, v in edges:
            g0[u].append(v)
            g0[v].append(u)

        g = [[] for _ in range(n)]
        def dfs(u: int, fa: int):
            for v in g0[u]:
                if v == fa:
                    continue
                g[u].append(v)
                dfs(v, u)
        dfs(0, -1)

        @cache
        def f(u: int, p: int, d: int) -> int:
            res1 = nums[u] * (-1 if p & 1 else 1)
            for v in g[u]:
                res1 += f(v, p, min(d + 1, k - 1))
            if d == k - 1:
                res2 = nums[u] * (1 if p & 1 else -1)
                for v in g[u]:
                    res2 += f(v, p ^ 1, 0)
                return max(res1, res2)
            else:
                return res1
        return f(0, 0, k - 1)

class Solution3:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        pa = [-1] * n
        def dfs(u: int, fa: int):
            for v in g[u]:
                if v == fa:
                    continue
                pa[v] = u
                dfs(v, u)
        dfs(0, -1)

        memo = [[[float('-inf')] * k for _ in range(2)] for _ in range(n)]
        q = deque([u for u, d in enumerate(deg) if d == 1 and u != 0])
        while q:
            u = q.popleft()
            for p in range(2):
                for d in range(k):
                    res1 = nums[u] * (-1 if p & 1 else 1)
                    for v in g[u]:
                        if v == pa[u]:
                            continue
                        res1 += memo[v][p][min(d + 1, k - 1)]
                    memo[u][p][d] = res1
                d = k - 1
                res2 = nums[u] * (1 if p & 1 else -1)
                for v in g[u]:
                    if v == pa[u]:
                        continue
                    res2 += memo[v][p ^ 1][0]
                memo[u][p][d] = max(memo[u][p][d], res2)
            deg[pa[u]] -= 1
            if pa[u] != 0 and deg[pa[u]] == 1 or pa[u] == 0 and deg[pa[u]] == 0:
                q.append(pa[u])
        return memo[0][0][k - 1]
    
# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.subtreeInversionSum([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [4,-8,-6,3,7,-2,5], 2))  # 27
print(sol.subtreeInversionSum([[0,1],[1,2],[2,3],[3,4]], [-1,3,-2,4,-5], 2))  # 9
print(sol.subtreeInversionSum([[0,1],[0,2]], [0,-1,-2], 3))  # 3
print(sol.subtreeInversionSum([[0,1],[1,2]], [-2,-4,3], 9))  # 3
print(sol.subtreeInversionSum([[3,1],[2,1],[2,5],[4,0],[0,6],[6,5]], [1,-2,0,-4,-5,5,5], 36))  # 22





