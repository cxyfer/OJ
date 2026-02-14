import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
先轉化問題，一條路徑能夠被重新排列成回文，當且僅當其中出現奇數次的字元最多只有一個。
由於我們只關注奇偶性，因此可以狀態壓縮，用 26 位二進制數表示每個字元出現的奇偶性。
又令 W[u] 表示 u 壓縮後的狀態，即 W[u] = 1 << (ord(s[u]) - ord('a'))。
那麼我們便可以只關注路徑上 W 的 XOR 和。

先思考不修改時要怎麼求 (u, v) 的路徑的 XOR 和，
令 f[u] 表示從根節點到 u 的路徑的 XOR 和，則 (u, v) 的路徑的 XOR 和為 f[u] ^ f[v] ^ W[LCA(u, v)]。
其中 f[lca(u, v)] 被計算了兩次，因此會被消除，我們需要補上 W[lca(u, v)] 來得到正確答案。

到這裡已經可以作為週賽的 Hard 題了，但這題還需要支持修改操作。
當我們修改 W[u] 時，會影響 u 的子樹中的 f[v] 的值，其中 v 是 u 的子樹中的節點。
而透過 DFN 序我們可以將子樹操作轉換為區間操作，因此我們可以使用線段樹來維護 f。
"""


class LCA:
    def __init__(self, g: List[List[int]]):
        n = len(g)
        self.m = m = n.bit_length()

        dep = [0] * n
        pa = [[-1] * m for _ in range(n)]  # pa[u][i] 表示 u 的第 2^i 個祖先

        def dfs(u: int, fa: int) -> None:
            """遞迴寫法"""
            pa[u][0] = fa
            for v in g[u]:
                if v == fa:
                    continue
                dep[v] = dep[u] + 1
                dfs(v, u)
        dfs(0, -1)

        # 用倍增法更新 pa
        for i in range(m - 1):
            for u in range(n):
                if pa[u][i] != -1:
                    pa[u][i + 1] = pa[pa[u][i]][i]

        self.dep = dep
        self.pa = pa

    # 返回 u 的第 k 個祖先
    def get_kth_ancestor(self, u: int, k: int) -> int:
        while k and u != -1:  # 當 u 被更新成 -1 後，可能會訪問到錯誤的位置，提前退出
            lb = k & -k
            u = self.pa[u][lb.bit_length() - 1]
            k &= k - 1
        return u

    # 返回 u 和 v 的 LCA
    def get_lca(self, u: int, v: int) -> int:
        if self.dep[u] > self.dep[v]:
            u, v = v, u
        # 使 v 和 u 在同一深度
        v = self.get_kth_ancestor(v, self.dep[v] - self.dep[u])
        if v == u:
            return u
        for i in range(self.m - 1, -1, -1):
            fu, fv = self.pa[u][i], self.pa[v][i]
            if fu != fv:  # 同時往上跳 2^i 步後還不會相遇
                u, v = fu, fv
        return self.pa[u][0]  # 再往上跳一步就是答案

    # 返回 u 到 v 的距離
    def get_dis(self, u: int, v: int) -> int:
        return self.dep[u] + self.dep[v] - self.dep[self.get_lca(u, v)] * 2


class SegNode:
    def __init__(self) -> None:
        self.ls = self.rs = None  # left and right child
        self.val = self.lazy = 0  # value, lazy tag


class SegmentTree:
    def __init__(self, nums: List[int] = None):
        self.nums = nums
        self.root = SegNode()
        if nums is not None and len(nums) > 0:
            self.build(self.root, 1, len(nums))

    def build(self, node: SegNode, left: int, right: int) -> None:
        if left == right:
            node.val = self.nums[left - 1]
            return
        mid = (left + right) // 2
        node.ls = SegNode()
        node.rs = SegNode()
        self.build(node.ls, left, mid)
        self.build(node.rs, mid + 1, right)
        self.pushup(node)  # push up node value

    # update the range [l, r] with value v
    @staticmethod
    def update(node: SegNode, left: int, right: int, l: int, r: int, v: int) -> None:
        if l <= left and right <= r:
            # update node value (Customized)
            SegmentTree._update(node, left, right, v)
            return
        SegmentTree.pushdown(node, left, right)  # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            SegmentTree.update(node.ls, left, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, right, l, r, v)
        SegmentTree.pushup(node)  # push up node value

    # update node value (Customized)
    @staticmethod
    def _update(node: SegNode, left: int, right: int, v: int) -> None:
        if (right - left + 1) & 1:
            node.val ^= v
        node.lazy ^= v

    # query the range [l, r]
    @staticmethod
    def query(node: SegNode, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return node.val
        # Ensure all lazy tags have been pushed down
        SegmentTree.pushdown(node, left, right)
        mid = (left + right) // 2
        # Calculate answer (Customized)
        ans = 0
        if l <= mid:
            ans ^= SegmentTree.query(node.ls, left, mid, l, r)
        if r > mid:
            ans ^= SegmentTree.query(node.rs, mid + 1, right, l, r)
        return ans

    # push down lazy tags
    @staticmethod
    def pushdown(node: SegNode, left: int, right: int) -> None:
        if node.ls is None:
            node.ls = SegNode()
        if node.rs is None:
            node.rs = SegNode()
        if node.lazy != 0:
            # Update node value (Customized)
            mid = (left + right) // 2
            SegmentTree._update(node.ls, left, mid, node.lazy)
            SegmentTree._update(node.rs, mid + 1, right, node.lazy)
            node.lazy = 0

    # push up node value
    @staticmethod
    def pushup(node: SegNode) -> None:
        # Update method (Customized)
        node.val = node.ls.val ^ node.rs.val


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        lca = LCA(g)

        # W[u] 表示 u 的權值
        W = [1 << (ord(c) - ord('a')) for c in s]

        f = [0] * n  # f[u] 表示 u 到根的路徑的 XOR 和
        dfns = [0] * n  # dfns[u] 表示 u 的 DFS 序開始時間
        dfne = [0] * n  # dfne[u] 表示 u 的 DFS 序結束時間
        time = 0

        def dfs(u, fa, val):
            nonlocal time
            time += 1
            dfns[u] = time
            val ^= W[u]
            f[u] = val
            for v in g[u]:
                if v == fa:
                    continue
                dfs(v, u, val)
            dfne[u] = time
            return val
        dfs(0, -1, 0)

        # 使用線段樹維護 f，轉換為 DFS 序後的序列以方便將子樹操作轉換為區間操作
        data = [-1] * n
        for u in range(n):
            data[dfns[u] - 1] = f[u]
        seg = SegmentTree(data)

        ans = []
        for q in queries:
            op, *args = q.split()
            if op == "update":
                u, c = int(args[0]), args[1]
                val = 1 << (ord(c) - ord('a'))
                if val != W[u]:
                    seg.update(seg.root, 1, n, dfns[u], dfne[u], val ^ W[u])
                    W[u] = val
            else:
                u, v = map(int, args)

                l = lca.get_lca(u, v)
                fu = seg.query(seg.root, 1, n, dfns[u], dfns[u])
                fv = seg.query(seg.root, 1, n, dfns[v], dfns[v])
                msk = fu ^ fv ^ W[l]
                ans.append(msk == 0 or msk.bit_count() == 1)
        return ans


sol = Solution()
print(sol.palindromePath(3, [[0, 1], [1, 2]], "aac", [
      "query 0 2", "update 1 b", "query 0 2"]))  # [true,false]

print(sol.palindromePath(4, [[0, 1], [0, 2], [0, 3]], "abca", [
      # [false,false,true]
      "query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]))
