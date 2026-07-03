#
# @lc app=leetcode id=3620 lang=python3
#
# [3620] Network Recovery Pathways
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n, m = len(online), len(edges)
        g = [[] for _ in range(n)]

        min_w, max_w = inf, -inf
        for u, v, w in edges:
            if online[u] and online[v]:
                g[u].append((v, w))
                min_w = min(min_w, w)
                max_w = max(max_w, w)

        if m == 0:
            return -1

        def check(mid: int):
            dist = [inf] * n
            dist[0] = 0
            hp = [(0, 0)]
            while hp:
                d, u = heappop(hp)
                if d > dist[u]:
                    continue
                if u == n - 1:
                    break
                for v, w in g[u]:
                    if w < mid or not online[v]:
                        continue
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(hp, (nd, v))
            return dist[n - 1] <= k

        left, right = min_w, max_w
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right if right >= min_w else -1


class Solution2:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n, m = len(online), len(edges)
        g = [[] for _ in range(n)]

        min_w, max_w = inf, -inf
        for u, v, w in edges:
            if online[u] and online[v]:
                g[u].append((v, w))
                min_w = min(min_w, w)
                max_w = max(max_w, w)

        if m == 0:
            return -1

        def check(mid: int):
            @cache
            def dfs(u: int) -> int:
                if u == n - 1:
                    return 0
                res = inf
                for v, w in g[u]:
                    if w < mid or not online[v]:
                        continue
                    res = min(res, dfs(v) + w)
                return res

            return dfs(0) <= k

        left, right = min_w, max_w
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right if right >= min_w else -1


class Solution3:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        n, m = len(online), len(edges)
        g = [[] for _ in range(n)]
        indeg = [0] * n

        if m == 0:
            return -1

        min_w, max_w = inf, -inf
        for u, v, w in edges:
            if online[u] and online[v]:
                g[u].append((v, w))
                indeg[v] += 1
                min_w = min(min_w, w)
                max_w = max(max_w, w)

        q = deque([u for u in range(1, n) if indeg[u] == 0])
        while q:
            u = q.popleft()
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        orders = []
        q = deque([0])
        while q:
            u = q.popleft()
            orders.append(u)
            for v, w in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def check(mid: int):
            f = [inf] * n
            f[0] = 0
            for u in orders:
                for v, w in g[u]:
                    if w >= mid:
                        f[v] = min(f[v], f[u] + w)
            return f[n - 1] <= k

        left, right = min_w, max_w
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right if right >= min_w else -1


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end


sol = Solution()
print(sol.findMaxPathScore([[1,2,90],[0,2,78]], [True, True, True], 145))  # 78
print(sol.findMaxPathScore([[2,3,22],[0,2,4],[1,2,42]], [True, True, True, True], 36))  # 4