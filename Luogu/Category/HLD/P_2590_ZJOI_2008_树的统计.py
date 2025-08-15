"""
P2590 [ZJOI2008] 树的统计
https://www.luogu.com.cn/problem/P2590
樹鏈剖分 + 線段樹

Python TLE
"""
import sys
from typing import List
sys.setrecursionlimit(int(5e5))

# 樹鏈剖分
class Node:
    def __init__(self, val: int = 0, fa: int = 0, dep: int = 0, sz: int = 0, son: int = 0, top: int = 0, dfn: int = 0):
        self.val = val
        self.fa = fa
        self.dep = dep
        self.sz = sz
        self.son = son
        self.top = top
        self.dfn = dfn

# 線段樹
class SegNode:
    def __init__(self, s: int = 0, mx: int = float("-inf")):
        self.s = s
        self.mx = mx

    def __add__(self, other):
        return SegNode(self.s + other.s, max(self.mx, other.mx))

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums) - 1
        self.nums = nums
        self.tree = [SegNode() for _ in range(4 * self.n)]
        self.build(1, 1, self.n)

    def build(self, o, left, right) -> None:  # node, left, right
        if left == right:  # Leaf node initialization
            self.tree[o].s = self.nums[left]
            self.tree[o].mx = self.nums[left]
            return
        mid = (left + right) // 2
        self.build(o << 1, left, mid)
        self.build(o << 1 | 1, mid + 1, right)
        self.pushup(o)

    def pushup(self, o) -> None:
        self.tree[o].s = self.tree[o << 1].s + self.tree[o << 1 | 1].s
        self.tree[o].mx = max(self.tree[o << 1].mx, self.tree[o << 1 | 1].mx)

    def _update(self, o, left, right, idx, val) -> None:
        if left == right:
            self.tree[o].s = val
            self.tree[o].mx = val
            return
        mid = (left + right) // 2
        if idx <= mid:
            self._update(o << 1, left, mid, idx, val)
        else:
            self._update(o << 1 | 1, mid + 1, right, idx, val)
        self.pushup(o)

    def _query(self, o, left, right, l, r) -> SegNode:
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid:
            return self._query(o << 1, left, mid, l, r)
        if mid < l:
            return self._query(o << 1 | 1, mid + 1, right, l, r)
        return self._query(o << 1, left, mid, l, mid) + self._query(o << 1 | 1, mid + 1, right, mid + 1, r)

    def update(self, idx, val) -> None:
        self._update(1, 1, self.n, idx, val)

    def query(self, l, r) -> SegNode:
        return self._query(1, 1, self.n, l, r)
    
def solve():
    n = int(input())
    A = [Node() for _ in range(n + 1)]
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    for u, val in enumerate(list(map(int, input().split())), 1):
        A[u].val = val

    def dfs1(u: int, fa: int) -> None:
        A[u].fa = fa
        A[u].dep = A[fa].dep + 1
        A[u].sz = 1
        for v in g[u]:
            if v == fa: continue
            dfs1(v, u)
            A[u].sz += A[v].sz
            if A[u].son == 0 or A[A[u].son].sz < A[v].sz:
                A[u].son = v
    dfs1(1, 0)

    dfn = 1
    idxs = [0] * (n + 1)
    def dfs2(u: int, top: int) -> None:
        nonlocal dfn
        if u == 0: return
        A[u].top = top
        A[u].dfn = dfn
        idxs[dfn] = u
        dfn += 1
        dfs2(A[u].son, top)
        for v in g[u]:
            if v == A[u].fa or v == A[u].son: continue
            dfs2(v, v)
    dfs2(1, 1)

    vals = [0] * (n + 1)
    for i in range(1, n + 1):
        vals[A[i].dfn] = A[i].val
    seg = SegmentTree(vals)

    def query(x: int, y: int) -> SegNode:
        ans = SegNode()
        while A[x].top != A[y].top:
            if A[A[x].top].dep >= A[A[y].top].dep:
                ans += seg.query(A[A[x].top].dfn, A[x].dfn)
                x = A[A[x].top].fa
            else:
                ans += seg.query(A[A[y].top].dfn, A[y].dfn)
                y = A[A[y].top].fa
        l, r = min(A[x].dfn, A[y].dfn), max(A[x].dfn, A[y].dfn)
        ans += seg.query(l, r)
        return ans

    m = int(input())
    for _ in range(m):
        op, *args = input().split()
        if op == "QMAX":
            x, y = map(int, args)
            print(query(x, y).mx)
        elif op == "QSUM":
            x, y = map(int, args)
            print(query(x, y).s)
        elif op == "CHANGE":
            x, y = map(int, args)
            seg.update(A[x].dfn, y)

if __name__ == "__main__":
    solve()