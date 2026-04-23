#
# @lc app=leetcode id=3590 lang=python3
#
# [3590] Kth Smallest Path XOR Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n = len(par)
        g = [[] for _ in range(n)]
        for i, fa in enumerate(par):
            if fa != -1:
                g[fa].append(i)

        ans = [-1] * len(queries)
        qs = [[] for _ in range(n)]
        for qid, (u, k) in enumerate(queries):
            qs[u].append((qid, k))

        def dfs(u: int, xor: int) -> SortedSet:
            xor ^= vals[u]

            st = SortedSet([xor])
            for v in g[u]:
                st2 = dfs(v, xor)
                if len(st2) > len(st):
                    st, st2 = st2, st
                st.update(st2)

            for qid, k in qs[u]:
                if k <= len(st):
                    ans[qid] = st[k - 1]
            return st

        dfs(0, 0)
        return ans
# @lc code=end

