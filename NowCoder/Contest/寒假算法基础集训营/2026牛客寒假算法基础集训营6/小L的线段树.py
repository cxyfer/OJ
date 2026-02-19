"""
C. 小L的线段树
https://ac.nowcoder.com/acm/contest/120566/C
"""


class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        size = 1 << (n.bit_length() + 1)
        self.tree = [1] * size
        self.bad = [False] * size

    def pushup(self, o: int) -> None:
        if self.bad[o]:
            self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]
        else:
            self.tree[o] = 1

    def _update(self, o: int, left: int, right: int, l: int, r: int) -> None:
        if left == l and right == r:
            self.bad[o] = True
            self.pushup(o)
            return
        mid = (left + right) // 2
        if r <= mid:
            self._update(o * 2, left, mid, l, r)
        else:
            self._update(o * 2 + 1, mid + 1, right, l, r)
        self.pushup(o)

    def update(self, l: int, r: int) -> None:
        self._update(1, 1, self.n, l, r)

    def _query(self, o: int, left: int, right: int, l: int, r: int) -> int:
        if l <= left and right <= r:
            return self.tree[o]
        mid = (left + right) // 2
        res = 1 if not self.bad[o] else 0
        if l <= mid:
            res += self._query(o * 2, left, mid, l, r)
        if r > mid:
            res += self._query(o * 2 + 1, mid + 1, right, l, r)
        return res

    def query(self, l: int, r: int) -> int:
        return self._query(1, 1, self.n, l, r)


def solve():
    n = int(input())
    seg = SegmentTree(n)
    for _ in range(n):
        op, l, r = map(int, input().split())
        if op == 1:
            seg.update(l, r)
        else:
            print(seg.query(l, r))


if __name__ == "__main__":
    solve()
