"""
P1884 [USACO12FEB] Overplanting S
https://www.luogu.com.cn/problem/P1884
1. 離散化 + 二維差分
2. 掃描線 + LazySegTree
"""

from collections import defaultdict
from itertools import pairwise
from typing import Optional, Callable, Any


def solve1():
    q = int(input())
    rects = []

    Xs = set()
    Ys = set()

    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        assert x1 <= x2 and y2 <= y1
        # 整理成左下/右上邊界
        rects.append((x1, y2, x2, y1))
        Xs.add(x1)
        Xs.add(x2)
        Ys.add(y2)
        Ys.add(y1)

    # 離散化
    Xs = sorted(Xs)
    Ys = sorted(Ys)
    mpX = {x: i for i, x in enumerate(Xs, start=1)}
    mpY = {y: i for i, y in enumerate(Ys, start=1)}

    n, m = len(Xs), len(Ys)

    # diff[i][j] 表示壓縮座標點上的差分
    diff = [[0] * (m + 1) for _ in range(n + 1)]

    # 二維差分更新
    for x1, y1, x2, y2 in rects:
        diff[mpX[x1]][mpY[y1]] += 1
        diff[mpX[x2]][mpY[y1]] -= 1
        diff[mpX[x1]][mpY[y2]] -= 1
        diff[mpX[x2]][mpY[y2]] += 1

    # 二維前綴和還原矩陣
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]

    # 計算面積
    ans = 0
    for i in range(1, n):
        dx = Xs[i] - Xs[i - 1]
        for j in range(1, m):
            dy = Ys[j] - Ys[j - 1]
            if diff[i][j] > 0:
                ans += dx * dy
    print(ans)


"""
Lazy Segment Tree (array-based, recursive)
- Use o, 2*o, 2*o+1 as node indices
- customizable:
    S: segment value type
    F: lazy tag type
    op(S, S) -> S                 : merge two segment values
    e: S                          : identity element of op
    mapping(F, S, seglen) -> S    : apply lazy tag to a segment value
    composition(F, F) -> F        : compose two lazy tags (new on old)
    id_: F                        : identity element of composition
"""


class LazySegTree:
    def __init__(
        self,
        v: Optional[Any] = None,
        op: Optional[Callable[[Any, Any], Any]] = None,
        e: Any = 0,
        mapping: Optional[Callable[[Any, Any, int], Any]] = None,
        composition: Optional[Callable[[Any, Any], Any]] = None,
        id_: Any = 0,
    ):
        if v is None:
            self.nums = None
            self.n = 0
        elif isinstance(v, int):
            self.nums = None
            self.n = v
        else:
            self.nums = list(v)
            self.n = len(self.nums)

        self.op = (lambda a, b: a + b) if op is None else op
        self.e = e
        # mapping(f, x, seglen)
        self.mapping = (
            (lambda f, x, seglen: x + f * seglen) if mapping is None else mapping
        )
        self.composition = (lambda f, g: f + g) if composition is None else composition
        self.id = id_

        self.root = 1
        size = 1 << (self.n.bit_length() + 1)
        self.val = [self.e] * size
        self.lazy = [self.id] * size

        if self.nums is not None and self.n > 0:
            self.build(self.root, 1, self.n)

    def build(self, o: int, left: int, right: int) -> None:
        """Build tree from self.nums on interval [left, right]."""
        if left == right:
            self.val[o] = self.nums[left - 1]
            return
        mid = (left + right) // 2
        self.build(o * 2, left, mid)
        self.build(o * 2 + 1, mid + 1, right)
        self.pushup(o)

    def _update(self, o: int, left: int, right: int, f: Any) -> None:
        """Apply lazy tag f to node o covering [left, right]."""
        seglen = right - left + 1
        self.val[o] = self.mapping(f, self.val[o], seglen)
        self.lazy[o] = self.composition(f, self.lazy[o])

    def pushdown(self, o: int, left: int, right: int) -> None:
        """Push lazy tag at node o down to its children."""
        if self.lazy[o] == self.id or left == right:
            return
        mid = (left + right) // 2
        f = self.lazy[o]
        self._update(o * 2, left, mid, f)
        self._update(o * 2 + 1, mid + 1, right, f)
        self.lazy[o] = self.id

    def pushup(self, o: int) -> None:
        """Recompute node value from children."""
        self.val[o] = self.op(self.val[o * 2], self.val[o * 2 + 1])

    def update(self, o: int, left: int, right: int, l: int, r: int, f: Any) -> None:
        """Range apply: apply tag f on interval [l, r]."""
        if l <= left and right <= r:
            self._update(o, left, right, f)
            return
        self.pushdown(o, left, right)
        mid = (left + right) // 2
        if l <= mid:
            self.update(o * 2, left, mid, l, r, f)
        if r > mid:
            self.update(o * 2 + 1, mid + 1, right, l, r, f)
        self.pushup(o)

    def query(self, o: int, left: int, right: int, l: int, r: int) -> Any:
        """Range query: return op-aggregate on interval [l, r]."""
        if l <= left and right <= r:
            return self.val[o]
        self.pushdown(o, left, right)
        mid = (left + right) // 2
        ans = self.e
        if l <= mid:
            ans = self.op(ans, self.query(o * 2, left, mid, l, r))
        if r > mid:
            ans = self.op(ans, self.query(o * 2 + 1, mid + 1, right, l, r))
        return ans

    # ---------------- external aliases (public API) ----------------
    def apply(self, l: int, r: int, f: Any) -> None:
        """Apply tag f to interval [l, r], 1-indexed."""
        if self.n <= 0 or l > r:
            return
        self.update(self.root, 1, self.n, l, r, f)

    def prod(self, l: int, r: int) -> Any:
        """Query op-aggregate on interval [l, r], 1-indexed."""
        if self.n <= 0 or l > r:
            return self.e
        return self.query(self.root, 1, self.n, l, r)

    def all_prod(self) -> Any:
        """Return aggregate on [1, n]."""
        if self.n <= 0:
            return self.e
        return self.val[self.root]


def solve2():
    n = int(input())

    events = defaultdict(list)
    Ys = set()
    for _ in range(n):
        # 整理成左下/右上邊界
        x1, y2, x2, y1 = map(int, input().split())
        events[x1].append((y1, y2, 1))
        events[x2].append((y1, y2, -1))
        Ys.add(y1)
        Ys.add(y2)

    events = sorted(events.items())

    Ys = sorted(Ys)
    mp = {y: i for i, y in enumerate(Ys, start=1)}  # 1-indexed

    # data[i] 代表區間 [ys[i], ys[i + 1]) 的 (最小覆蓋次數, 對應長度)
    data = [(0, y2 - y1) for y1, y2 in pairwise(Ys)]
    tot_y = Ys[-1] - Ys[0]

    def op(a, b):
        if a[0] < b[0]:
            return a
        if a[0] > b[0]:
            return b
        return (a[0], a[1] + b[1])

    def mapping(f, x, seglen):
        # 區間覆蓋次數整體 + f，最小覆蓋次數會改變，但對應長度不變
        return (x[0] + f, x[1])

    def composition(f, g):
        return f + g

    seg = LazySegTree(
        data,
        op=op,
        e=(float("inf"), 0),
        mapping=mapping,
        composition=composition,
        id_=0,
    )

    ans = 0
    prev_x = events[0][0]
    for x, es in events:
        min_cover, min_cover_len = seg.all_prod()
        covered_y = tot_y - (min_cover_len if min_cover == 0 else 0)
        ans += covered_y * (x - prev_x)
        prev_x = x
        for y1, y2, delta in es:  # [y1, y2)
            seg.apply(mp[y1], mp[y2] - 1, delta)

    print(ans)


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
