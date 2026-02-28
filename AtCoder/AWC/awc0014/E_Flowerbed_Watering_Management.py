from typing import Any, Callable, Optional

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


class LazySegmentTree:
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


def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))

    seg = LazySegmentTree(A)

    for _ in range(q):
        op, *args = map(int, input().split())
        if op == 1:
            l, r, x = args
            seg.apply(l, r, x)
        else:
            l, r = args
            print(seg.prod(l, r))


if __name__ == "__main__":
    solve()
