from itertools import accumulate
# from atcoder.segtree import SegTree
import typing

class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = self._n.bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

n, q = map(int, input().split())
A = list(map(int, input().split()))

s = list(accumulate(A))
d = [0] * n
for i in range(1, n):
    d[i] = A[i] - s[i-1]  # 左邊還要增加多少個才能滿足這個位置的條件

st = SegTree(op=lambda x, y: max(x, y), e=float('-inf'), v=d)
for _ in range(q):
    l, r = map(lambda x: int(x) - 1, input().split())

    if l == r:
        print(0)
        continue

    ts = s[l-1] if l > 0 else 0
    mx = st.prod(l + 1, r + 1) # [l + 1, r]
    ans = abs(max(0, ts + mx))
    print(ans)